# 109. The same split, always

`random_state=0` everywhere is not superstition. It is so a colleague
can reproduce your number.

When you change the split, say so in the PR. Otherwise "AUC went up"
is a different test set.

Lab: already true in most labs. Habit: grep your capstone for
`train_test_split` and confirm `random_state` and `stratify`.

## Pass / fail

Capstone A split is frozen. Evaluate uses the same seed (it does).
