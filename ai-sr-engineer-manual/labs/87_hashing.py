from sklearn.feature_extraction.text import HashingVectorizer, TfidfVectorizer

texts = [
    "reset password login",
    "invoice march billing",
    "android crash settings",
] * 5
tfidf = TfidfVectorizer().fit_transform(texts)
h = HashingVectorizer(n_features=16, alternate_sign=False).transform(texts)
print("tfidf", tfidf.shape, "hash", h.shape)
assert h.shape[1] == 16
