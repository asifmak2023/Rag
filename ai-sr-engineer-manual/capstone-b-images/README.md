# Capstone B. Tiny image classifier

CPU-friendly CNN on synthetic 16x16 images (two classes). Swap in real
folders of `ok/` and `defect/` later. The training loop plus API is
the point.

## Run

```bash
pip install -r requirements.txt
python train.py
python infer.py
uvicorn serve:app --host 0.0.0.0 --port 8001
```

```bash
python -c "import json,numpy as np; print(json.dumps({'pixels': np.random.normal(size=256).tolist()}))" > /tmp/p.json
curl -s http://127.0.0.1:8001/predict -H 'content-type: application/json' --data @/tmp/p.json
```

Docker after `python train.py`:

```bash
docker build -t cnn-capstone:v1 .
docker run --rm -p 8001:8000 cnn-capstone:v1
```

## What you must be able to say

- Why conv + pool
- Why `eval()` + `no_grad()`
- Why this synthetic task is only a loop rehearsal, not a product
- How you would switch to a frozen ResNet18 head on real photos
