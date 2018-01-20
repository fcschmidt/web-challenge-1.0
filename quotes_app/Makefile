# Sample Makefile
# Used to install settings and dependencies
# Start DB and Run App
all: recipe

DEV=development.ini
PY=python3

recipe:
	make install
	make init_db
	make run

install:
	$(PY) setup.py develop

init_db:
	initialize_quotes_app_db $(DEV)

run:
	pserve $(DEV) --reload
