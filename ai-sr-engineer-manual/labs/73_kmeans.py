from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler

X, y = make_blobs(n_samples=600, centers=3, random_state=0)
Xs = StandardScaler().fit_transform(X)
km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(Xs)
print("inertia", float(km.inertia_))
print("crosstab counts")
print(confusion_matrix(y, km.labels_))
