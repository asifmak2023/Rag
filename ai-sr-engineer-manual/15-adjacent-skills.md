# 15. Adjacent skills the posting named (R, Java, C++, cloud)

You will not be hired as an R or Java engineer. You must not freeze if
they ask.

## R (one evening)

Enough to read a colleague's EDA:

```r
df <- read.csv("data.csv")
summary(df)
df$city <- factor(df$city)
model <- glm(y ~ x1 + x2, data=df, family=binomial)
```

Translation: `glm` ~ sklearn LogisticRegression, `dplyr` ~ pandas.
If they require R daily, this job posting would have led with it. It did
not. Python is the job.

## Java (one hour of talk)

Enterprise services are often Java. Your model still ships as:

- a REST service Java calls, or
- ONNX Runtime in a JVM, or
- a batch file Java already consumes

You do not rewrite PyTorch in Java. You define a stable JSON contract.

## C++ (use your past)

When they ask about speed:

- Profile Python first
- Vectorize
- Then Cython / pybind11 / a small C++ extension for the hot loop
- Serving 8-feature logistic regression in Python is already < 1 ms

Bring one story of a C++ or MATLAB routine you wrote that was
performance-sensitive. That is seniority.

## Cloud platforms

Learn the nouns, not the console clicks:

- VM + Docker is enough to explain v1
- Object storage for data and `model.joblib`
- Secret manager / env vars
- Load balancer, HTTPS, autoscaling later
- GPU instance only if you train large nets; most tabular serving is CPU

Pick one provider (whichever you can make a free account on) and push
one container. Write the URL in the capstone README if it stays up.
If you cannot host, a local Docker demo is honest and sufficient.

## Git, not optional

```bash
git checkout -b feat/churn-threshold
# work
git add -p
git commit -m "feat: pick churn threshold from precision floor"
```

Branches, small commits, PRs. Models are software.

## Communication artifacts they will like

- 1-page design note before you train
- PR description with metric table
- Incident note when the API 500s
- Weekly "what I would improve" (chapter 09 template)

Practice writing like an engineer, not like a blog.
