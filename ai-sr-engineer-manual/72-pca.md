# 72. PCA in 15 minutes

Center X. SVD. Principal axes = directions of max variance. Project
to k components. Used to plot, compress, sometimes denoise. Not a
substitute for domain features.

Lab 72. File: `labs/72_pca.py`

2D from 8D, print explained variance ratio sum of first 2.

Interview: "PCA is unsupervised. It does not know the label. It can
throw away a weak-variance feature that was the only useful one."

Pass / fail: PCA vs LDA in one line (LDA uses labels). You only need
the name of LDA.
