import torch

torch.manual_seed(0)
n, d = 256, 4
X = torch.randn(n, d)
true_w = torch.tensor([1.5, -2.0, 0.5, 0.25])
y = X @ true_w + 0.05 * torch.randn(n)


def fit(opt_name, steps=300):
    torch.manual_seed(1)
    w = torch.zeros(d, requires_grad=True)
    if opt_name == "sgd":
        opt = torch.optim.SGD([w], lr=0.05)
    else:
        opt = torch.optim.Adam([w], lr=1e-2)
    loss = None
    for _ in range(steps):
        loss = ((X @ w - y) ** 2).mean()
        opt.zero_grad()
        loss.backward()
        opt.step()
    return float(loss), w.detach().tolist()


for name in ("sgd", "adam"):
    loss, w = fit(name)
    print(name, "loss", round(loss, 5), "w", [round(v, 3) for v in w])
