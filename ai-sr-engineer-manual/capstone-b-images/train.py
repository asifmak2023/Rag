from pathlib import Path

import torch
from torch.utils.data import DataLoader, TensorDataset

from model import TinyCNN

ART = Path(__file__).resolve().parent / "artifacts"
ART.mkdir(exist_ok=True)


def make_data(n=800, seed=0):
    g = torch.Generator().manual_seed(seed)
    X = torch.randn(n, 1, 16, 16, generator=g)
    y = (X.mean(dim=(1, 2, 3)) > 0).long()
    return X, y


def main():
    X, y = make_data()
    Xtr, ytr, Xte, yte = X[:640], y[:640], X[640:], y[640:]
    loader = DataLoader(TensorDataset(Xtr, ytr), batch_size=32, shuffle=True)
    model = TinyCNN()
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = torch.nn.CrossEntropyLoss()
    history = []
    for epoch in range(12):
        model.train()
        total = 0.0
        for xb, yb in loader:
            opt.zero_grad()
            loss = loss_fn(model(xb), yb)
            loss.backward()
            opt.step()
            total += float(loss.detach()) * len(xb)
        model.eval()
        with torch.no_grad():
            val = float((model(Xte).argmax(1) == yte).float().mean())
        history.append((epoch, total / len(Xtr), val))
        print(f"epoch {epoch} train_loss {history[-1][1]:.4f} val_acc {val:.3f}")
    torch.save(
        {"state_dict": model.state_dict(), "history": history},
        ART / "cnn.pt",
    )


if __name__ == "__main__":
    main()
