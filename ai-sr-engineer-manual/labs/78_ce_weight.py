import torch
from torch import nn

logits = torch.tensor([[2.0, 0.1], [0.2, 1.5], [1.0, 1.1]])
y = torch.tensor([0, 1, 0])
plain = nn.CrossEntropyLoss()(logits, y)
n = torch.tensor([2.0, 1.0])
w = n.sum() / (2 * n)
weighted = nn.CrossEntropyLoss(weight=w)(logits, y)
print("plain", float(plain), "weighted", float(weighted), "w", w.tolist())
