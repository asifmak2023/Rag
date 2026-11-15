from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

X, y = make_classification(n_samples=3000, n_features=16, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)
scaler = StandardScaler().fit(Xtr)
Xtr, Xte = scaler.transform(Xtr), scaler.transform(Xte)

model = tf.keras.Sequential(
    [
        tf.keras.layers.Input(shape=(16,)),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation="sigmoid"),
    ]
)
model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="binary_crossentropy",
    metrics=["accuracy", tf.keras.metrics.AUC(name="auc")],
)
model.fit(
    Xtr,
    ytr,
    validation_split=0.2,
    epochs=8,
    batch_size=64,
    verbose=0,
)
loss, acc, auc = model.evaluate(Xte, yte, verbose=0)
print("loss", float(loss), "acc", float(acc), "auc", float(auc))
model.save("labs/keras_mlp.keras")
