# Rag

Job posting in `Ragdoc`. Training path in `ai-sr-engineer-manual/`.

Start: `ai-sr-engineer-manual/23-first-seven-days.md`

```bash
python3 -m venv ~/ai-env
source ~/ai-env/bin/activate
pip install -r ai-sr-engineer-manual/requirements-light.txt
python3 ai-sr-engineer-manual/labs/run_cpu_labs.py
```

Light sweep skips torch labs if torch is not installed.
CPU torch: `pip install torch --index-url https://download.pytorch.org/whl/cpu`
Then `cd ai-sr-engineer-manual && make test`.
Capstones: `ai-sr-engineer-manual/capstone-a-churn/` and `capstone-b-images/`.
