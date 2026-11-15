# 17. Images: CNNs and transfer learning

You already have the CNN class in chapter 04. This chapter is how a
consulting CV ticket actually looks: few images, class imbalance,
pretrained backbone, then an API that resizes bytes.

## Shapes (tattoo this)

PyTorch: `(N, C, H, W)`  e.g. `(32, 3, 224, 224)`
Keras:   `(N, H, W, C)`

MNIST gray: C=1. Phone photos: C=3, RGB.

## Lab 17A. Synthetic CNN that overfits on purpose

File: `labs/17_cnn_synthetic.py`

Tiny random images, 2 classes, a CNN that can memorize. You are proving
you can wire conv -> pool -> flatten -> linear and see train accuracy
climb. Then cut capacity or add dropout and watch the gap.

If you can download MNIST later, replace the random tensors. The loop
does not change.

## Lab 17B. Transfer learning script (read, then type)

```python
import torch
from torch import nn
from torchvision import models

class HeadResNet(nn.Module):
    def __init__(self, n_classes=2, freeze=True):
        super().__init__()
        backbone = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        in_f = backbone.fc.in_features
        backbone.fc = nn.Identity()
        if freeze:
            for p in backbone.parameters():
                p.requires_grad = False
        self.backbone = backbone
        self.head = nn.Linear(in_f, n_classes)

    def forward(self, x):
        return self.head(self.backbone(x))
```

Train head 3-10 epochs. Unfreeze last block. Drop lr 10x. That is 90%
of industrial image classification.

If torchvision weights cannot download in your network, keep the class,
train the CNN from lab 04 on synthetic data, and explain the freeze
protocol in the interview anyway.

## Augmentation (train only)

Flip, small crop, color jitter. Never augment the test set. Never
augment before the split in a way that leaks the same image into both
sides (copy-paste the same file into train and val).

## Inference API shape

- Client sends JPEG bytes or a URL your service fetches internally
- You resize to the training size, normalize with the same mean/std
- `model.eval()`; `torch.no_grad()`
- Return class name + probability, not a tensor dump

Mismatch of normalize stats between train and serve is silent death.

## Detection vs classification vs OCR

If they say "find the defect in the frame", that is detection (boxes),
not classification. Do not offer a softmax over the whole image as the
final design. Say: "I would start with classification if the photo is
already cropped; detection if the object must be found."

OCR is a separate stack. Name Tesseract / a CRNN as options. Do not
pretend you have shipped a custom OCR unless you have.

## Pass / fail

Draw a ResNet-head pipeline on paper, including freeze/unfreeze and the
exact tensor shape at the head. Write the eval() inference snippet from
memory.
