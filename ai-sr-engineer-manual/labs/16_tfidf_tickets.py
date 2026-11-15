from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

texts = [
    "cannot login password reset failed",
    "invoice not generated for march",
    "app crashes on android 14",
    "please reset my password urgently",
    "billing charged twice this month",
    "crash when opening settings",
    "otp not received login issue",
    "refund the extra invoice amount",
    "black screen after launch crash",
] * 8
labels = ["auth", "billing", "crash"] * 3 * 8

Xtr, Xte, ytr, yte = train_test_split(
    texts, labels, test_size=0.25, random_state=0, stratify=labels
)
pipe = Pipeline(
    [
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
        ("clf", LogisticRegression(max_iter=1000)),
    ]
)
pipe.fit(Xtr, ytr)
print(classification_report(yte, pipe.predict(Xte)))
print("example", pipe.predict(["password not working on login"])[0])
