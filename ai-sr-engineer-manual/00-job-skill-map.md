# 00. Job posting mapped to skills

Every line in Ragdoc is a skill you must be able to demonstrate, not recite.

## Role

Sr. Artificial Intelligence Engineer, Pivotize Consulting, Karachi.
Full-time, in person, Bahria Complex 1, Lalazar, M.T. Khan Road.
Pay from Rs 250,000 / month. No remote, no freelance, no online interview.

## What they actually hire for

They want someone who can sit with engineers, take a messy business problem,
turn it into data + a model + an API, and keep it running.

Your MCS already covers theory and programming. The gap is the Python ML
production loop. This table is the gap.

| Job line | What you must do with your hands | Chapter |
|---|---|---|
| Design AI solutions that integrate with products | Write a model, wrap it in FastAPI, call it from a fake product | 08, 11, 18 |
| Python, R, Java, C++ + TF / PyTorch / sklearn | Daily Python. Know when C++/MATLAB still win. TF and PyTorch both | 01, 04, 05, 15 |
| Collect, preprocess, analyze large data | pandas, sklearn pipelines, chunked CSV, SQL extracts | 03, 06 |
| Data cleaning, feature engineering, EDA | Missing values, leakage, encodings, plots you can defend | 03, 06 |
| Deploy: containers, microservices, cloud | Docker image, REST service, health checks, ONNX, API key | 08, 49, 50 |
| Test performance, reliability, security | Metrics, holdout, adversarial inputs, auth on the API | 07, 08 |
| Research and experiments | Baselines first, then ablations, then a written result | 10 |
| Monitor and recommend improvements | Logs, drift sketch, latency, error budget | 09 |
| Stay current | One paper or release note per week, one paragraph of impact | 10 |
| Degree CS/IT | You have MCS. State it cleanly | 12, 25 |
| 4+ years, Python/R/MATLAB | Translate MATLAB/C++ years into Python ML years with projects | 11, 12, 25 |
| Data science, linear algebra, algorithms, stats | Derivations you can do on a whiteboard in 10 minutes | 02, 24 |
| Large data streams, efficient code | Generators, chunking, vectorization, no Python loops on rows | 06 |
| DL/ML algorithms and frameworks | Logistic, trees, SVM, NB, kNN, PCA, k-means, NN, CNN, TF-IDF, GBDT | 03, 04, 05, 16, 17, 24, 33, 71, 72, 73 |
| Communication | One-page design notes, oral walkthrough of a model | 10, 12, 18, 25 |
| Current / expected salary, notice, onsite | Prepare numbers. Do not improvise in the room | 12, 14 |

## What "seasoned" looks like in an onsite room

You can, without looking anything up:

1. Load a CSV, find leakage, train a sklearn pipeline, report F1 with a
   confidence interval, and refuse a metric that does not match the business.
2. Write a PyTorch training loop from scratch: dataset, model, loss, step.
3. Explain vanishing gradients, dropout, batch norm, and learning rate in
   one minute each.
4. Put the model behind POST /predict, Dockerize it, and describe how you
   would watch it in production.
5. Say "I would not use a neural net here" and justify it with data size.

If you cannot do those five, you are not ready. The rest of this manual
exists only to make those five automatic.

## How your existing skills transfer

| You already have | How a Sr. AI engineer uses it |
|---|---|
| C / C++ | NumPy is C under the hood. You write vectorized Python, drop to C++ only for hot loops. Know memory layout. |
| MATLAB | Matrices, broadcasting, plotting. NumPy/pandas is MATLAB with indexes and missing values. |
| SQL / DB programming | Feature stores start as SQL. Joins, window functions, leak-free time splits. |
| Algorithms / complexity | Why O(n log n) tree training beats naive loops. Why you batch. |
| Software engineering | Git, tests, modules, APIs. Models are software. |

Do not hide the MATLAB/C++ years. Reframe them: "I have N years writing
numerical and database code. The last 16 weeks I rebuilt that stack in
Python ML and shipped two production-style systems."

## Languages they listed

- Python: primary. Every lab.
- R: optional. Know dplyr-level EDA if asked. Not required daily.
- Java: know it exists in enterprise serving. You will serve with Python.
- C++: performance story, not your daily serving language.
- MATLAB: your past. Translate examples, do not submit MATLAB for this job.

## Frameworks they listed

- scikit-learn: first tool for tabular. You must be fluent.
- PyTorch: first tool for deep learning. You must write training loops.
- TensorFlow / Keras: second DL tool. You must train and export a Keras model.

You will be competent in all three. PyTorch is the one you speak first.
