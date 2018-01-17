#!/bin/bash
#
# Install and configure project
python3 setup.py develop

# Create and init  data base
initialize_quotes_app_db development.ini

# Start app
pserve development.ini --reload
