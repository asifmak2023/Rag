# 79. Transfer learning checklist (onsite)

Chapter 17 had the class. This is the talk.

1. Pick a backbone trained on a similar domain (ImageNet for photos).
2. Replace the head for your n_classes.
3. Freeze backbone, train head, higher lr.
4. Unfreeze last block, 10x lower lr.
5. Augment train only. Same normalize as pretraining (ImageNet mean/std
   if that is what the weights expect).
6. If n is tiny, stay frozen longer. If n is huge, you can train more.

NLP analog: freeze BERT, train classifier on [CLS]; then unfreeze last
layers. Domain mismatch (tweets vs Wikipedia) is the failure mode.

## Pass / fail

Freeze then unfreeze, two learning rates, ImageNet normalize. No notes.
