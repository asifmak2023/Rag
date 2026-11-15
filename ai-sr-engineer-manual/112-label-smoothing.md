# 112. Label smoothing (know the knob)

Replace one-hot 1 with `1 - e`, and 0 with `e / (k-1)`. Stops the net
from becoming insanely confident. Related to temperature (105) but
happens at train time.

PyTorch: `CrossEntropyLoss(label_smoothing=0.1)`.

Do not smooth tabular GBDT labels as a first trick. Do not smooth
fraud labels if 1 really means 1.

## Pass / fail

You can say "it regularizes overconfidence during training".
