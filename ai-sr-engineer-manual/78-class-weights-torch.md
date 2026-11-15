# 78. Class weights in PyTorch

sklearn `class_weight="balanced"`. Torch: `CrossEntropyLoss(weight=w)`
where w is a tensor of size n_classes, larger on the rare class.

```python
import torch
from torch import nn
n = torch.tensor([900.0, 100.0])
w = n.sum() / (2 * n)
loss_fn = nn.CrossEntropyLoss(weight=w)
```

This changes the training objective. You still pick a threshold on
probabilities for the product (chapter 51). Do not skip the threshold.

Focal loss: name it for dense detectors. Not needed for capstone A.

## Pass / fail

You can write the weight formula `n / (k * n_c)` and put it in
CrossEntropyLoss.
