# 19. Interview answers (speak these, do not read them)

Short answers. If they want depth, they will ask. Practice out loud.

## 1. Bias vs variance

Bias: the model is too simple, systematic error, underfit.
Variance: the model jumps when the sample jumps, overfit.
High bias: add features or a richer model.
High variance: more data, regularization, simpler model, dropout.

## 2. Why k-fold leaks in time series

Fold 3 may contain Tuesday, fold 1 Friday of the same week. The model
sees the future through correlated neighbors. Use a cutoff time. Train
before T, validate after T. Purged k-fold only if you know the embargo.

## 3. Precision vs recall for fraud

Precision: of flagged cases, how many were fraud. Low precision wastes
investigators.
Recall: of actual fraud, how many you caught. Low recall leaks money.
Set a precision floor the ops team can live with, then maximize recall.

## 4. L1 vs L2

L2 (Ridge): shrinks weights, keeps all features, stable when collinear.
L1 (Lasso): drives some weights to zero, feature selection.
Elastic net: both. Neural nets usually L2 / weight decay.

## 5. Gradient descent, two audiences

PM: "We measure error, then nudge knobs to reduce it, a little at a
time, like tuning a radio."
Engineer: "w := w - lr * dL/dw. Mini-batch SGD estimates the gradient
from a batch. Adam adapts per-parameter step sizes."

## 6. Why ReLU

Cheap, sparse activations, avoids saturating like sigmoid in deep
stacks. Dying ReLU: leaky ReLU or GELU. Sigmoid stays on the output for
binary probability.

## 7. Dropout train vs eval

Train: randomly zero units, force redundancy.
Eval: use all units, scaled. `model.eval()` in PyTorch does this.
If you forget, production scores are noisy.

## 8. Batch norm

Normalize activations per batch, then learn scale and shift. Faster,
stabler training. At eval, use running mean/var, not the batch of one
request. Another reason for `model.eval()`.

## 9. Learning rate

Too big: loss NaN or explodes. Too small: flat line.
Start 1e-3 Adam, 0.1 SGD with momentum for from-scratch CNNs.
LR finder or a few powers of 10. Reduce on plateau. Fine-tune heads at
1e-3, unfrozen backbone at 1e-4 or 1e-5.

## 10. When GBDT beats a net

Tabular, < few million rows, mixed types, missing values, need
feature importance tomorrow. Nets win on raw images, audio, language,
or when you have huge data and a representation to learn.

## 11. Data drift next month

Log feature means, PSI vs training window, output score histogram.
If PSI > ~0.2 on a driver feature, slice metrics by week. Do not
retrain on a timer with no evaluation.

## 12. Serve a 500 MB PyTorch model

`eval`, `no_grad`, load once at startup, warmup dummy batch, pin
memory if GPU. Quantize or distill if p95 misses SLA. Do not load
weights per request. Horizontal scale replicas behind a load balancer.

## 13. pickle vs state_dict vs ONNX

pickle/joblib: sklearn Pipeline, Python-only, unsafe from the network.
state_dict: PyTorch weights + your class code.
ONNX: portable runtime, Java/C++ can score, ops must be exportable.

## 14. Training-serving skew

Different code paths. Fix: one `build_features(row)` used in train and
serve, tested. Same scaler, same vocabulary, same image size.

## 15. Imbalance, three methods

class_weight / sample_weight: first lever.
Threshold on probability: first lever that changes the product.
Resample (SMOTE etc.): last, can leak or invent nonsense.
Also: better features, more real minority data.

## 16. Embedding

A vector for an entity (word, sentence, user) such that geometry
matches similarity. Learned from data. Downstream: cosine, or a
classifier on the vector.

## 17. Attention in four sentences

Each token makes query, key, value.
Score = query dot keys; softmax; weighted sum of values.
A token can pull information from any other token in the window.
Multi-head: several of these in parallel.

## 18. A/B a model

Randomize at the unit you care about (user, not request).
Same traffic mix. Primary metric + guardrails (latency, complaints).
Run until sample size, not until it looks good. Canary then 100%.

## 19. Never unpickle user uploads

Pickle can execute code. Model artifacts are trusted only if you built
them. Accept JSON features, not serialized Python objects.

## 20. A model I would not ship

99% accuracy on 1% fraud with no PR curve. Or a net on 400 rows. Or an
API without schema checks. Or a score used to deny loans with no
fairness slice and no human appeal.

## Salary / onsite (fill blanks, speak once)

Current: ________
Expected: Rs ________ to ________ because onsite production AI + MCS.
Notice: ________
Onsite: Yes. Bahria Complex 1. No remote request.
