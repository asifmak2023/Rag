# 12. Onsite interview at Bahria Complex 1

Mandatory on-site. No remote, no online assessment. Treat the commute
and the room as part of the exam.

Address to know: Bahria Complex 1, Lalazar, M.T. Khan Road, Karachi.
Visit once before the interview if you can so the day is not your first
time in that traffic.

## Application questions (write answers now)

Do this on paper. Do not invent numbers in the lobby.

1. Current salary: exact monthly take-home and gross. If unemployed, say
   last drawn and date.
2. Expected salary: a range, not a single shot. Floor at or above the
   posting's "From Rs 250,000". If you want 350k, say 300-350k and why
   (onsite, production AI, MCS).
3. Notice period: true number. If you can join in 2 weeks, say 2 weeks.
4. Commute / onsite: "Yes. I can attend onsite interviews and work in
   person at Bahria Complex 1. I am not seeking remote or freelance."

They stated no freelance and no online. Do not ask for hybrid in round 1.

## What a Sr. AI Engineer interview usually is

Expect some mix of:

- HR screen on salary, notice, onsite (you already prepared)
- Technical talk: past work + these two capstones
- Live coding: pandas + sklearn, or a PyTorch loop on a whiteboard
- ML design: "We have X, build a system"
- Culture: can you sit with software engineers and not only data people

## Live coding drills (do each twice with a timer)

45 minutes, no internet except docs if they allow.

1. Load CSV, clean, Pipeline, F1, print two mistakes you avoided.
2. Write PyTorch MLP train loop on random tensors.
3. SQL: last 30 day aggregates per user without future leak.
4. FastAPI stub with Pydantic, even if they only want pseudocode.

## Twenty questions you must answer out loud

Practice standing, 90 seconds each.

1. Bias vs variance. Draw it.
2. Why k-fold can leak in time series.
3. Precision vs recall for fraud.
4. What is regularization. L1 vs L2.
5. Explain gradient descent to a PM, then to an engineer.
6. Why ReLU. Why not sigmoid in hidden layers.
7. Dropout at train vs eval.
8. Batch norm in one minute.
9. How you choose a learning rate.
10. When GBDT beats a neural net.
11. How you would detect data drift next month.
12. How you would serve a 500 MB PyTorch model.
13. pickle vs state_dict vs ONNX.
14. How you prevent training-serving skew.
15. Class imbalance: three methods, when each fails.
16. What is an embedding.
17. Attention in four sentences.
18. How you would A/B test a model.
19. Security: why you never unpickle user uploads.
20. Tell me about a model you would not ship.

## Design prompt (rehearse this exact one)

"A bank wants to score loan applications in under 200 ms. 2 million
historical rows, 40 features, 5% default. Build it."

Your answer structure:

1. Metric: recall at a precision the risk team sets, not accuracy.
2. Split by time.
3. Baseline logistic, then GBDT.
4. Features from SQL, point-in-time.
5. Pipeline in one artifact.
6. API p95 < 200 ms, CPU is enough.
7. Monitor default rate vs score band.
8. Humans in the loop for borderline scores.
9. Risks: bias by city/income, rejected applications not in training.

Timebox to 8 minutes. Then shut up.

## MATLAB / C++ question

They may ask why you are not an ML specialist already.

"I built numerical and database systems first. Linear algebra and
performance were the job. I moved that discipline onto Python, sklearn,
and PyTorch, and I ship models as services. I still drop to C++ thinking
when I profile."

Then show Capstone A.

## Day-of checklist

- Printed CV, one page extra on the two capstones
- Laptop with env working, Docker image loaded, airplane mode demo
- Numbers: salary, notice, join date
- CNIC, copies, whatever HR asked
- Arrive early. Onsite means onsite.

## After

Write what they asked, the same day. That list is your next study plan.

## Pass / fail for week 16

You can give the bank design talk, the 20 answers, and a 5-minute
capstone demo without notes. Salary and onsite answers are written.
