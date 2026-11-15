from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_classification(
    n_samples=1200,
    n_features=10,
    n_informative=6,
    n_classes=3,
    n_clusters_per_class=1,
    weights=[0.6, 0.3, 0.1],
    random_state=0,
)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
pipe = Pipeline(
    [("sc", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]
)
pipe.fit(Xtr, ytr)
pred = pipe.predict(Xte)
print(classification_report(yte, pred))
print("macro", float(f1_score(yte, pred, average="macro")))
print("weighted", float(f1_score(yte, pred, average="weighted")))
