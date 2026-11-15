# 62. Regularization picture (one page)

You will draw this.

```
too simple ---- sweet spot ---- too wiggly
underfit         good            overfit
high bias                     high variance
train error high              train error ~0
val error high                val error high
```

Knobs toward simpler: smaller trees, fewer leaves, more min_child,
stronger L2, dropout, more data, early stop, smaller net.

Knobs toward flexible: opposite.

L1 vs L2: chapter 19. Elastic net: both.

Neural nets: weight decay is L2. Dropout is noise. Batch norm is not
primarily a regularizer even if it sometimes acts like one. Do not
mix the story.

## Pass / fail

Draw train vs val curves for the three regimes. 60 seconds.
