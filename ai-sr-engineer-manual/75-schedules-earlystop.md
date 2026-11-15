# 75. Learning-rate schedules and early stopping

A constant lr is a baseline. A schedule is how you finish training.

## Common schedules

- Step: drop lr by 10x every N epochs
- Cosine: smooth decay to a floor
- Reduce on plateau: if val loss stalls, divide lr

Keras: `ReduceLROnPlateau`. PyTorch: `StepLR`, `CosineAnnealingLR`.

## Early stopping

Save best `state_dict` by val loss. Stop after `patience` epochs of
no improvement. Restore best. This is regularization (chapter 62).

## Lab 75. File: `labs/75_early_stop.py`

Toy loop: val loss is a U shape you fake or get from a slightly
overfit MLP. Implement patience=3. Print the epoch you restore.

## Pass / fail

You never say "I trained 100 epochs" without a val curve or early stop.
