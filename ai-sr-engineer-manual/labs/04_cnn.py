import torch
from torch import nn


class SmallCNN(nn.Module):
    def __init__(self, n_classes=10):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(32 * 7 * 7, n_classes),
        )

    def forward(self, x):
        return self.net(x)


model = SmallCNN()
x = torch.randn(4, 1, 28, 28)
logits = model(x)
print("logits", tuple(logits.shape))
assert logits.shape == (4, 10)
