# 60. Transformers and "LLMs" without pretending

You will be asked. Answer like an engineer who ships classifiers.

## What you must be able to say

- Transformer: attention, chapter 19 Q17
- BERT-like: pretrained encoder, fine-tune a head, or freeze and embed
- GPT-like: decoder, next-token, good at text generation, expensive
  and slippery for a 200 ms risk score
- Token: subword piece, not a word
- Context window: max tokens in, truncation exists
- RAG: retrieve documents, then generate. The repo is named Rag. If
  they ask, "retrieval plus generation; the quality is the retriever
  and the corpus, not the logo on the LLM"

## What you will not do for Pivotize v1

- Train a 7B model from scratch
- Put an LLM on the loan decision path without an audit score
- Scrape the open web as a feature store

## When an LLM is reasonable

- Draft a support reply with a human send button
- Extract fields from messy PDFs, then validate with regex/schema
- Bootstrap labels, then train a small classifier

## Pass / fail

90 seconds: transformer vs GBDT vs LLM for (a) churn table (b) tickets
(c) a chatbot. Correct mapping, no hype.
