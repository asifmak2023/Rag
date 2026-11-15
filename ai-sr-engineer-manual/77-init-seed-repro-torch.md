# 77. Init, seed, cudnn, still not bit-exact

`nn.Linear` uses kaiming/uniform variants by default. You rarely write
Xavier by hand in 2026. You do set seeds (chapter 48).

GPU nondeterminism: atomic adds, cudnn benchmarks. For this job, CPU
plus seed is enough. If they ask: `torch.use_deterministic_algorithms`
can break some ops.

Dropout + seed: still random per forward in train mode. Eval is
deterministic given weights.

## Pass / fail

`train()` vs `eval()` with dropout: two different mean outputs on the
same batch (drill C7). Repeat if rusty.
