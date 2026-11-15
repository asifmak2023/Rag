import torch
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

X, y = make_classification(n_samples=3000, n_features=16, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)
scaler = StandardScaler().fit(Xtr)
Xtr = torch.tensor(scaler.transform(Xtr), dtype=torch.float32)
Xte = torch.tensor(scaler.transform(Xte), dtype=torch.float32)
ytr = torch.tensor(ytr, dtype=torch.long)
yte = torch.tensor(yte, dtype=torch.long)

loader = DataLoader(TensorDataset(Xtr, ytr), batch_size=64, shuffle=True)
model = nn.Sequential(
    nn.Linear(16, 32),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(32, 2),
)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

for _ in range(15):
    model.train()
    for xb, yb in loader:
        opt.zero_grad()
        loss = loss_fn(model(xb), yb)
        loss.backward()
        opt.step()

model.eval()
with torch.no_grad():
    acc = (model(Xte).argmax(1) == yte).float().mean()
print("acc", float(acc))
