# 111. One-pass mean and variance (Welford)

Chapter 06 said you do not need the whole file in RAM. Welford updates
mean and variance in one stream. Interview gold for "large data
streams at speed".

```
count += 1
delta = x - mean
mean += delta / count
delta2 = x - mean
M2 += delta * delta2
variance = M2 / count          # population
# sample variance: M2 / (count-1)
```

Numerically better than `sum` and `sumsq` on large streams.

## Lab 111. File: `labs/111_welford.py`

Stream a numpy array, match `mean` and `var` (ddof=0).

## Pass / fail

Write the four lines on a whiteboard. Say why two-pass is simpler but
needs a rewind.
