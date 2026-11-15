# Capstone B report

## Problem

Binary classification on 16x16 single-channel images. Synthetic labels
are "mean pixel > 0". This is a loop rehearsal, not a factory product.

## Method

TinyCNN: conv 8, pool, conv 16, pool, linear 2.
Adam 1e-3, 12 epochs, CPU. Saved `state_dict` only.

## Serving

FastAPI `/predict` takes 256 floats, reshapes to `(1,1,16,16)`,
`eval()` + `no_grad()`, warmup at startup.

## What I would change on real photos

- Folders `ok/` and `defect/`, ImageFolder, 224 resize
- Frozen ResNet18 head, then unfreeze last block
- Augment train only
- Compare against a logistic on flattened pixels (the dumb baseline)

## Spoken walkthrough

Shapes, why conv, why eval, why this data is fake, how I would not
claim CV experience until real images exist.
