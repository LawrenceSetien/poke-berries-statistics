#!/bin/bash

echo "######################## Starting app container ########################"
echo "######################## Env mode: $ENV_MODE"


if [ "$ENV_MODE" = 'prod' ]; then
    # Starting flask in prod mode
    exec gunicorn --workers 4 --threads 2 --bind 0.0.0.0:5000 app:app
else
    # Starting flask in dev mode
    exec flask run --host=0.0.0.0 --port=5000 --debug
fi
