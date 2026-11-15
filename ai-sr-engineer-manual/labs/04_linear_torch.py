import torch

torch.manual_seed(0)
n, d = 256, 3
X = torch.randn(n, d)
true_w = torch.tensor([2.0, -1.0, 0.5])
y = X @ true_w + 0.1 * torch.randn(n)

w = torch.zeros(d, requires_grad=True)
b = torch.zeros((), requires_grad=True)
opt = torch.optim.SGD([w, b], lr=0.05)

loss = None
for _ in range(400):
    pred = X @ w + b
    loss = ((pred - y) ** 2).mean()
    opt.zero_grad()
    loss.backward()
    opt.step()

print("w", w.detach().tolist(), "b", float(b.detach()), "loss", float(loss.detach()))
