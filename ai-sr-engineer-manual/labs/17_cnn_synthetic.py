import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(0)
n, h, w = 400, 16, 16
X = torch.randn(n, 1, h, w)
y = (X.mean(dim=(1, 2, 3)) > 0).long()
Xtr, Xte = X[:320], X[320:]
ytr, yte = y[:320], y[320:]
loader = DataLoader(TensorDataset(Xtr, ytr), batch_size=32, shuffle=True)


class TinyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 8, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(8, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(16 * 4 * 4, 2),
        )

    def forward(self, x):
        return self.net(x)


model = TinyCNN()
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()
for _ in range(8):
    model.train()
    for xb, yb in loader:
        opt.zero_grad()
        loss = loss_fn(model(xb), yb)
        loss.backward()
        opt.step()

model.eval()
with torch.no_grad():
    acc = (model(Xte).argmax(1) == yte).float().mean()
print("test acc", float(acc))
