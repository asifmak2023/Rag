# 74. Optimizers: SGD, momentum, Adam

You already run `Adam`. Say what it is.

## SGD

`w -= lr * grad`. Noisy if mini-batch. Noise can help escape sharp
minima. Needs a well-tuned lr.

## Momentum

Keep a velocity. Like a ball rolling. Smoother, faster on ravines.

## Adam

Per-parameter adaptive rates using first and second moment of
gradients, with bias correction. Default lr 1e-3 is a starting point,
not a law. Weight decay: prefer AdamW if you speak modern PyTorch
(`torch.optim.AdamW`).

## When SGD still wins

Large CNN from scratch, long training, careful schedule. For your
capstones, Adam is fine.

## Lab 74. File: `labs/74_sgd_vs_adam.py`

Fit the same torch linear model with SGD and Adam. Print final loss.
Do not overclaim; one toy is not a paper.

## Interview extra

Gradient clipping: `clip_grad_norm_` when RNNs explode. Batch size vs
lr: bigger batch, often bigger lr (linear scaling rule, approximate).

## Pass / fail

Name SGD, momentum, Adam, AdamW. Say default Adam lr without looking.
