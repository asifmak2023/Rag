from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X, y = make_classification(n_samples=800, n_features=8, n_informative=3, random_state=0)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=2, random_state=0).fit(Xs)
print("explained", pca.explained_variance_ratio_.tolist())
print("sum2", float(pca.explained_variance_ratio_.sum()))
Z = pca.transform(Xs)
print("Z", Z.shape)
