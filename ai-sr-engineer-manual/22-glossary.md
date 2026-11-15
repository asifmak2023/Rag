# 22. Glossary you must not mix up

| Term | Meaning in this job |
|---|---|
| Feature | An input column the model is allowed to see |
| Label / target | What you predict |
| Grain | What one row represents |
| Leakage | Information the model would not have at prediction time |
| Baseline | The simple model you must beat |
| Pipeline | Preprocess + model as one object |
| Holdout | Data you touch once at the end |
| Calibration | Do 0.8 scores happen ~80% of the time |
| Serving | Running the model for a product |
| Batch vs online | Nightly table vs per-request API |
| Drift | World changed, model did not |
| Embedding | Dense vector for similarity or as features |
| Epoch | One pass over the training set |
| Batch | Slice of data in one update |
| Logits | Raw scores before softmax/sigmoid |
| state_dict | Weight tensors of a PyTorch module |
| p95 latency | 95% of calls faster than this |
| Champion / challenger | Live model vs candidate |
| Point-in-time | Features computed only from the past |
| Class weight | Penalize errors on the rare class more |

If you use "AI" in a sentence, replace it with the actual thing:
classifier, regressor, ranker, detector, or generative model. Precision
in language is seniority.
