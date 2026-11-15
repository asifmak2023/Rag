# 29. Fairness, privacy, product sense (Karachi onsite)

A Sr. AI Engineer who only talks AUC is a risk. The posting says
security and communication. This is that.

## Fairness (practical, not a TED talk)

If a score affects people (loan, job, policing, pricing):

- Slice metrics by city, gender if you have it, age band, tenure.
- A model that is strong overall and terrible in Quetta or for seniors
  is not done.
- Removing the sensitive column does not fix it if proxies remain
  (area, device, income).
- You do not secretly collect gender to "debug fairness" without a
  legal/product owner.

Interview sentence: "I report slice metrics and refuse to ship a
score used for denial without a human appeal path."

## Privacy

- CNIC, phone, name: not in logs, not in git, not in notebooks you
  copy to USB.
- Aggregate in SQL when you can.
- If they ask you to scrape customer WhatsApp: no.

## Security already in chapter 07, plus

- Model inversion / membership inference: know the words. For a churn
  GBDT on 40 features, not your first worry. For an API that echoes
  embeddings of private documents, it is.
- Dependency pins. A surprise `pip install` on the server is an
  incident.

## Product sense questions you ask in the first meeting

1. What decision changes if the score is 0.4 vs 0.8?
2. Who is blamed when it is wrong?
3. When do labels arrive?
4. What is the latency budget?
5. What did they do before ML?

If they cannot answer 1, do not train.

## Consulting behavior at Pivotize

You will sit with software engineers. Translate:

- "We need two weeks of labels and a batch table, not a neural net."
- "I can put a logistic API in a container this week. Boosting after
  the metric is agreed."
- Write the design note before the code.

## Pass / fail

You can refuse a project politely and propose a smaller v1. Rehearse
that sentence.
