#!/bin/bash

source .env

export PYTHONPATH='./berries_app'

# Run the tests from test_unittesting.py
pytest "$PROJECT_PATH"/poke-berries-statistics/berries_app/unittests -vv

# Run the smoke tests
python -m unittest discover -s "$PROJECT_PATH"/poke-berries-statistics/tests -vv
