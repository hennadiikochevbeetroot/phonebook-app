.DEFAULT_GOAL := run

run:
	python cli.py

test:
	pytest app/tests
