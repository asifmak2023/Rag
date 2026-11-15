# 113. Checkpoints (resume without tears)

Save every N epochs:

```
{
  epoch,
  model_state,
  optimizer_state,
  rng_state,
  best_val,
  config
}
```

If the VM dies at epoch 47, you do not start at 0. `state_dict` of
the optimizer matters (Adam moments).

Capstone B already saves `state_dict`. Upgrade: save optimizer too
if you train longer than 12 toy epochs.

## Pass / fail

"I save model + optimizer + epoch + seed."
