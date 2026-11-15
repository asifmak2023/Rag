# 04. PyTorch: the deep learning tool you speak first

Keras hides the loop. Seniors write the loop. That is PyTorch.

## Tensors

A tensor is a NumPy array that can live on GPU and track gradients.

```python
import torch
x = torch.tensor([[1., 2.], [3., 4.]], requires_grad=True)
y = (x ** 2).sum()
y.backward()
print(x.grad)  # 2x
```

Device:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = x.to(device)
```

CPU is enough for this manual. If you have a GPU, same code.

## Lab 04A. Linear regression in pure torch

File: `labs/04_linear_torch.py`

```python
import torch
torch.manual_seed(0)
n, d = 256, 3
X = torch.randn(n, d)
true_w = torch.tensor([2., -1., 0.5])
y = X @ true_w + 0.1 * torch.randn(n)

w = torch.zeros(d, requires_grad=True)
b = torch.zeros((), requires_grad=True)
opt = torch.optim.SGD([w, b], lr=0.05)

for step in range(400):
    pred = X @ w + b
    loss = ((pred - y) ** 2).mean()
    opt.zero_grad()
    loss.backward()
    opt.step()
print(w.detach(), b.detach(), float(loss))
```

Self-check: what happens if you forget `zero_grad`? Try it. Gradients
accumulate. Remember that sentence.

## The training loop (memorize this skeleton)

```python
model.train()
for xb, yb in loader:
    xb, yb = xb.to(device), yb.to(device)
    opt.zero_grad()
    logits = model(xb)
    loss = loss_fn(logits, yb)
    loss.backward()
    opt.step()
```

Eval:

```python
model.eval()
with torch.no_grad():
    ...
```

If you cannot write that from memory, you cannot claim PyTorch.

## Lab 04B. Dataset, DataLoader, MLP classifier

File: `labs/04_mlp_tabular.py`

```python
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=3000, n_features=16, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)
sc = StandardScaler().fit(Xtr)
Xtr = torch.tensor(sc.transform(Xtr), dtype=torch.float32)
Xte = torch.tensor(sc.transform(Xte), dtype=torch.float32)
ytr = torch.tensor(ytr, dtype=torch.long)
yte = torch.tensor(yte, dtype=torch.long)

loader = DataLoader(TensorDataset(Xtr, ytr), batch_size=64, shuffle=True)

model = nn.Sequential(
    nn.Linear(16, 32),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(32, 2),
)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(15):
    model.train()
    for xb, yb in loader:
        opt.zero_grad()
        loss = loss_fn(model(xb), yb)
        loss.backward()
        opt.step()

model.eval()
with torch.no_grad():
    acc = (model(Xte).argmax(1) == yte).float().mean()
print(float(acc))
```

## Lab 04C. CNN on synthetic images (or MNIST if downloaded)

File: `labs/04_cnn.py`

```python
import torch
from torch import nn

class SmallCNN(nn.Module):
    def __init__(self, n_classes=10):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(32 * 7 * 7, n_classes),  # 28x28 in, two pools
        )

    def forward(self, x):
        return self.net(x)
```

If you cannot fetch MNIST, generate `torch.randn(n, 1, 28, 28)` and
random labels. You are practicing the API, then later train on real data.

Things you must be able to explain while pointing at this class:

- Why conv vs linear on images (weight sharing, locality)
- What 16 and 32 are (channels)
- Why pooling (downsample, some invariance)
- Shape arithmetic: 28 -> 14 -> 7

## Lab 04D. Overfit then regularize

1. Tiny model, huge data: underfit. Train and val loss both high.
2. Huge model, tiny data: overfit. Train loss ~0, val loss up.
3. Add dropout, weight decay (`Adam(..., weight_decay=1e-4)`), early
   stopping on val loss.

Draw the curves. Photograph them into your notes.

## Transfer learning (interview gold)

You rarely train ImageNet from scratch. You take a pretrained backbone,
replace the head, freeze then unfreeze.

Pattern:

```python
# pseudo
backbone.requires_grad_(False)
head = nn.Linear(backbone.out_dim, n_classes)
# train head
backbone.requires_grad_(True)
# train all at lower lr
```

Know the names: ResNet, EfficientNet, ViT, BERT, sentence-transformers.
You do not need to implement them.

## Saving

```python
torch.save(model.state_dict(), "cnn.pt")
model.load_state_dict(torch.load("cnn.pt", map_location="cpu"))
model.eval()
```

Save `state_dict` plus a `config.json` of input shape and class names.
Saving the whole pickle of a class is fragile.

## Common crashes you must recognize

| Symptom | Cause |
|---|---|
| Loss is NaN | lr too big, log(0), exploding grad |
| Loss never moves | lr too small, forgot train(), wrong labels dtype |
| Acc 10% on 10 classes | chance. model not learning |
| Train acc 100, val 50 | overfit |
| CUDA out of memory | batch too big |
| Slow epoch | DataLoader `num_workers=0` on large disk data |

## Pass / fail

Pass if you can write, blank file, in 25 minutes:

- nn.Module with conv or linear
- DataLoader
- train loop with zero_grad / backward / step
- eval with no_grad
- save and load state_dict
