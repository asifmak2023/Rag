.PHONY: light labs test

light:
	python3 -m pip install -r requirements-light.txt

labs:
	python3 labs/run_cpu_labs.py

test:
	python3 -m pytest labs/tests -q
	python3 -m pytest labs/churn_proto/tests -q
	python3 -m pytest capstone-a-churn/tests -q
