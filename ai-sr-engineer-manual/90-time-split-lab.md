# 90. Time split, coded (not just talked)

Chapter 41 said it. This lab fails if you shuffle.

## Lab 90. File: `labs/90_time_split.py`

Rows with dates. Split at a cutoff. Assert max(train.ts) < min(test.ts).
Then a shuffled split that violates it, so you see the bug.

## Pass / fail

One assert on time order in every dated project.
