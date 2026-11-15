from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

X, y = make_classification(n_samples=1500, n_features=12, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=0)
models = {
    "logreg": Pipeline(
        [("sc", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]
    ),
    "nb": GaussianNB(),
    "linearsvc": Pipeline(
        [("sc", StandardScaler()), ("m", LinearSVC(max_iter=4000))]
    ),
}
for name, m in models.items():
    m.fit(Xtr, ytr)
    print(name, float(f1_score(yte, m.predict(Xte))))
