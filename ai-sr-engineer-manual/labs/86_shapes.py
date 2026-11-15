import torch
from torch import nn

x = torch.randn(8, 1, 28, 28)
layers = [
    nn.Conv2d(1, 16, 3, padding=1),
    nn.MaxPool2d(2),
    nn.Conv2d(16, 32, 3, padding=1),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(32 * 7 * 7, 10),
]
for i, layer in enumerate(layers):
    x = layer(x)
    print(i, type(layer).__name__, tuple(x.shape))
assert tuple(x.shape) == (8, 10)
