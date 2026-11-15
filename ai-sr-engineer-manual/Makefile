.PHONY: light labs test test-light

light:
	python3 -m pip install -r requirements-light.txt

labs:
	python3 labs/run_cpu_labs.py

test-light:
	python3 -m pytest labs/tests -q
	python3 -m pytest labs/churn_proto/tests -q
	python3 -m pytest capstone-a-churn/tests -q

test: test-light
	python3 -m pytest capstone-b-images/tests -q
