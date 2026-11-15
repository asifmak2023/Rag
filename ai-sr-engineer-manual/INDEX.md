# Read order

Start here if you are lost.

1. `23-first-seven-days.md` — this week
2. `00-job-skill-map.md` — why each chapter exists
3. Chapters `01` to `10` in number order
4. `16` NLP and `17` CV during weeks 7-8
5. `capstone-a-churn/` then `capstone-b-images/`
6. `18` design, `19` answers, `20` drills, `21` katas
7. `12` + `14` in the 10 days before Bahria Complex 1
8. `25` before you send the CV
9. `24` + `22` whenever a term is fuzzy
10. `26` if MATLAB is still your first language
11. `27` `28` `29` before onsite
12. `30` mock day, `31` if they ask about month one
13. `32` SQL features (you should be strong here already)
14. `33` GBDT / LightGBM, `34` calibration
15. `35` git, `36` Linux, `37` resources
16. `38` self-audit before you apply
17. `39` spoken scripts, `40` lab ticks
18. `41` time series, `42` ranking, `43` batch scoring
19. `44` stats, `45` feature store lite, `46` error table
20. `47` onsite logistics for Bahria Complex 1
21. `48` seeds/versions, `49` ONNX, `50` API key
22. `51` imbalance, `52` EDA tour
23. `53` pytest, `54` JSON logs, `55` model card
24. `56` train config, `57` metrics from scratch, `58` ensembles
25. `59` labels, `60` transformers/LLM honesty
26. `61` CV types, `62` regularization picture
27. `63` schema contract, `64` profiling, `65` weekly demos
28. `66` log loss, `67` missing, `68` outliers, `69` encoding
29. `70` scaling, `71` kNN/NB/SVM, `72` PCA, `73` k-means
30. `74` optimizers, `75` schedules/early stop, `76` gradients
31. `77` torch seed, `78` CE weights, `79` transfer talk, `80` A/B
32. `81` ROC/PR, `82` regression metrics, `83` multiclass
33. `84` feature select, `85` pipeline memory, `86` CNN shapes
34. `87` hashing, `88` cosine/RAG retrieval, `89` cost threshold
35. `90` time-split assert, `91` dummy baselines

Install light (no torch/tf) for weeks 1-4:

```bash
pip install -r requirements-light.txt
```

CPU lab sweep: `python labs/run_cpu_labs.py` (needs the venv).
Skip `05_keras_mlp.py` until TensorFlow is installed.
