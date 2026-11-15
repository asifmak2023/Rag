# 05. TensorFlow / Keras: the second framework they named

You will not be a TF specialist. You will be able to train, export, and
read a Keras model so you are not blocked if their stack is TF.

Keras is the API. TensorFlow is the engine.

## Lab 05A. Same MLP as chapter 04, in Keras

File: `labs/05_keras_mlp.py`

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

X, y = make_classification(n_samples=3000, n_features=16, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)
sc = StandardScaler().fit(Xtr)
Xtr, Xte = sc.transform(Xtr), sc.transform(Xte)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(16,)),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])
model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="binary_crossentropy",
    metrics=["accuracy", tf.keras.metrics.AUC(name="auc")],
)
cb = [
    tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
    tf.keras.callbacks.ModelCheckpoint("keras_mlp.keras", save_best_only=True),
]
model.fit(
    Xtr, ytr,
    validation_split=0.2,
    epochs=20,
    batch_size=64,
    callbacks=cb,
    verbose=2,
)
print(model.evaluate(Xte, yte, verbose=0))
```

Self-check: `Sequential` vs functional API. Rewrite this with:

```python
inp = tf.keras.Input(shape=(16,))
x = tf.keras.layers.Dense(32, activation="relu")(inp)
out = tf.keras.layers.Dense(1, activation="sigmoid")(x)
model = tf.keras.Model(inp, out)
```

Functional API is what you use when there are two inputs.

## Lab 05B. CNN in Keras

```python
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(28, 28, 1)),
    tf.keras.layers.Conv2D(16, 3, padding="same", activation="relu"),
    tf.keras.layers.MaxPool2D(2),
    tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu"),
    tf.keras.layers.MaxPool2D(2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
```

Channels-last `(H, W, C)` is Keras default. PyTorch is channels-first
`(C, H, W)`. Mixing them is a classic production bug.

## Export

```python
model.save("saved_model_dir")          # SavedModel, serving
model.export("export_dir")             # newer TF
# or ONNX via tf2onnx when you need a shared runtime
```

Interview sentence: "I train in Keras, export SavedModel or ONNX, serve
with TF Serving or a Python process. For a consulting shop I usually
serve with FastAPI unless they already have TF Serving."

## PyTorch vs TensorFlow (have a grown-up answer)

| | PyTorch | TensorFlow / Keras |
|---|---|---|
| Research / custom loops | Default | Possible, more ceremony |
| Keras convenience | Lightning exists | Built-in |
| Mobile / TFLite | ExecuTorch, newer | Mature TFLite |
| Hiring market 2024-2026 | Stronger in new teams | Strong in older enterprise |

Say: "I am fluent in both. I prototype in PyTorch. I can maintain Keras."

## Pass / fail

Train a Keras model, save it, load it in a new process, run `predict`
on one batch. If that fails, you are not done.
