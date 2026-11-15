import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    "reset my password I cannot login",
    "invoice and billing charged twice",
    "the app crashes on android",
]
q = ["password login failed"]
vec = TfidfVectorizer().fit(docs)
D = vec.transform(docs)
Q = vec.transform(q)
sims = cosine_similarity(Q, D)[0]
print("sims", np.round(sims, 3), "best", int(sims.argmax()), docs[int(sims.argmax())])
assert int(sims.argmax()) == 0
