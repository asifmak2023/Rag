# 36. Linux CLI enough for an onsite AI engineer

You will ssh into a box or open a terminal in the office. MATLAB GUI
will not save you.

## Daily

```bash
pwd
ls -la
cd
cat
less
head
tail -n 50
mkdir -p
cp
mv
chmod +x
```

Disk and process:

```bash
df -h
free -h
ps aux
top
```

Do not run `rm -rf`. Move to a backup folder if you must "delete".

## Data peek without pandas

```bash
wc -l data.csv
head -n 5 data.csv
cut -d, -f1,4 data.csv | head
```

Python still wins for real parsing. CLI is for "is this file empty".

## Python env

```bash
python3 -m venv ~/ai-env
source ~/ai-env/bin/activate
pip install -r requirements-light.txt
python labs/run_cpu_labs.py
deactivate
```

## Docker

```bash
docker build -t churn-capstone:v1 capstone-a-churn
docker run --rm -p 8000:8000 churn-capstone:v1
docker ps
docker logs
```

If Docker is missing, uvicorn is enough to demo.

## Git

Chapter 35. `status`, `diff`, `log`, `add -p`, `commit`.

## curl

```bash
curl -s http://127.0.0.1:8000/health
curl -s http://127.0.0.1:8000/predict \
  -H 'content-type: application/json' \
  -d '{"tenure_months":12,"monthly_charges":85,"total_charges":1020,"contract":"month-to-month","internet":"fiber","senior":0}'
```

## Pass / fail

Without a GUI: create venv, run a lab, curl a local API. Time limit
20 minutes once the service exists.
