# Sample Makefile
# Used to install settings and dependencies
# Start DB and Run App

DEV=development.ini
PY=python3

install:
	$(PY) setup.py develop

init_db:
	initialize_quotes_app_db $(DEV)

run:
	pserve $(DEV) --reload
