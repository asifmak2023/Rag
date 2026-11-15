# 76. Vanishing and exploding gradients

Deep sigmoid nets: gradients shrink layer by layer (vanishing). Unstable
RNNs: gradients blow up (exploding).

Fixes you must name:

- ReLU (and friends) instead of sigmoid in hidden layers
- Initialization (He/Xavier) — PyTorch defaults are reasonable
- Residual connections (ResNet): add skip so gradients have a highway
- Batch norm
- Gradient clipping
- LSTM/GRU gates, or just use a transformer / shorter sequences
- Lower lr

Lab: no extra file required. In `04_linear_torch.py` you already saw
NaN if lr is insane. Try `lr=10` once, watch loss explode, write the
number in notes.

## Pass / fail

One minute: vanishing vs exploding, two fixes each.
