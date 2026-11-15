from pathlib import Path

import torch

from model import TinyCNN

ART = Path(__file__).resolve().parent / "artifacts" / "cnn.pt"


def load_model():
    bundle = torch.load(ART, map_location="cpu", weights_only=False)
    model = TinyCNN()
    model.load_state_dict(bundle["state_dict"])
    model.eval()
    return model


def main():
    model = load_model()
    x = torch.randn(1, 1, 16, 16)
    with torch.no_grad():
        prob = torch.softmax(model(x), dim=1)[0]
    print("p_class1", float(prob[1]), "label", int(prob.argmax()))


if __name__ == "__main__":
    main()
