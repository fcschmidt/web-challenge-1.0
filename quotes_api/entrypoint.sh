#!/bin/bash
#
# Install and configure project
python3 setup.py develop

# Start app
pserve development.ini --reload
