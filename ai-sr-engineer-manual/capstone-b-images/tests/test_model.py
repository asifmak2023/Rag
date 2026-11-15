import torch

from model import TinyCNN


def test_forward_shape():
    m = TinyCNN()
    m.eval()
    x = torch.zeros(2, 1, 16, 16)
    with torch.no_grad():
        y = m(x)
    assert tuple(y.shape) == (2, 2)
