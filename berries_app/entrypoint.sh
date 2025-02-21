#!/bin/bash

echo "Starting app container"
exec flask run --host=0.0.0.0 --port=5000 --debug
