# 16. Text models (tickets, search, classification)

Consulting AI often means: classify support tickets, detect spam, tag
documents. Start linear. Deep models only after TF-IDF loses.

## Lab 16A. TF-IDF + logistic (this is the baseline)

File: `labs/16_tfidf_tickets.py`

```python
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
pipe = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
    ("clf", LogisticRegression(max_iter=1000)),
])
pipe.fit(Xtr, ytr)
print(classification_report(yte, pipe.predict(Xte)))
print(pipe.predict(["password not working on login"]))
```

Interview: "I ship TF-IDF + linear unless the error analysis shows
paraphrase / multilingual problems the bag-of-words cannot see."

## What TF-IDF is (say it in 40 seconds)

Term frequency: how often a word appears in this document.
Inverse document frequency: down-weight words that appear in every
document. A document becomes a sparse vector. A linear model draws a
hyperplane in that space. ngrams capture "not working".

## Lab 16B. Error analysis before deep learning

Print 20 mistakes. Bucket them:

- synonym the vocab missed
- two intents in one message
- language mix (roman Urdu + English)
- too short
- label noise

Only if synonyms and paraphrase dominate do you go to embeddings.

## Embeddings (know, then use a library)

A sentence embedding is a dense vector such that similar meaning is
nearby. Cosine similarity is the score.

You do not train BERT from scratch. You call a pretrained encoder.

Pattern:

```python
# pseudo: sentence-transformers
# emb = model.encode(texts)   # (n, 384)
# LogisticRegression on emb, or cosine to class prototypes
```

If the package is not installed, skip the code and still explain:

- Frozen encoder + linear head is transfer learning for text
- Fine-tuning is slower, easier to overfit on 2k tickets
- Max length, truncation, and domain mismatch (Wikipedia vs bank tickets)

## Lab 16C. Training-serving skew on text

Train-time: `TfidfVectorizer.fit` on train only.
Serve-time: that same vocabulary. If you refit on new data inside the
API, vectors move and the classifier is garbage.

Save the whole Pipeline. Same rule as chapter 03.

## When they mention ChatGPT / LLMs

Have a senior answer:

"An LLM is a component, not the architecture. For a 6-class ticket
router with 50k labeled rows, TF-IDF or a small classifier is cheaper,
faster, and auditable. I would use an LLM for unlabeled bootstrapping
or messy extraction, with a human or regex check, not as the only
production path for a latency-sensitive score."

Do not lead a bank-risk design with "call an LLM".

## Pass / fail

From raw strings, in 30 minutes: Pipeline, report, one example
prediction, and a written note on two failure modes.
