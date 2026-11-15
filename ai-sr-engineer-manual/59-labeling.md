# 59. Labels: the part everyone skips

Garbage labels beat fancy models. Consulting projects die here.

## Ask

- Who labeled, with what instruction sheet?
- Double-labeled agreement (Cohen's kappa if they know it; % agree if not)
- Can the label leak from a comment field?
- Delay: fraud confirmed 60 days later

## Weak labels

Rules, regex, "if amount > X". Use as noisy pretraining or to filter,
not as gospel. Record that they are weak.

## Active learning (name only)

Score unlabeled, pick uncertain or high-impact rows for humans.
Useful when labeling is expensive. Not week 1.

## Interview

"I will spend a day on the label definition before I tune depth."

## Pass / fail

You ask "what is a positive?" before you ask "GPU or CPU?"
