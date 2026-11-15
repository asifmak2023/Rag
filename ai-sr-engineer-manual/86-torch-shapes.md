# 86. Shape table drill (CNN)

Fill this on paper for 28x28 gray, batch 8:

| layer | in | out |
|---|---|---|
| input | 8,1,28,28 | |
| conv 16, k=3, pad=1 | | 8,16,28,28 |
| pool 2 | | 8,16,14,14 |
| conv 32, k=3, pad=1 | | 8,32,14,14 |
| pool 2 | | 8,32,7,7 |
| flatten | | 8, 1568 |
| linear 10 | | 8,10 |

Formula pad=1, k=3, stride=1: spatial size unchanged.
Pool 2 stride 2: halves.

Lab 86. File: `labs/86_shapes.py` already close to `04_cnn.py`. Print
shapes with a forward hook or just sequential prints.

## Pass / fail

No calculator, 28->14->7, 32*7*7=1568.
