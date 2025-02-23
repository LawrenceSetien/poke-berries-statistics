# Prerequisites

- Ubuntu 22.04
- Docker version 27.5.1
- Docker Compose version v2.32.4

# Start your venv
```sh
# Create your venv
python3 -m venv venv

# Start it
source venv/bin/activate

# Install required libraries
pip install -r berries_app/requirements.txt
```

# Instructions to start the app
1. Copy and rename `example.env` to `.env`
```sh
cp example.env .env
```

2. Update `PROJECT_PATH` in the `.env` to point where your project is.
**Note**: This is required to execute the tests.

3. Choose how to start the app (dev or prod mode) by changing the `ENV_MODE` variable.

4. Install the app:
```sh
bash install.sh
```

5. Run tests:
```sh
bash run_tests.sh
```

6. (Optional) Uninstall the app:
```sh
bash uninstall.sh
```

# Notes
- A postman collection was added to streamline the development process, you can find it on `postman_collection`.
- Three endpoints were created:
    - **GET /health_check**: A basic endpoint used by docker compose to check if the container is responding.
        - Live on: https://lawrencesetien.pythonanywhere.com/health_check
    - **GET /allBerryStats**: The main API, it returns the statistics of the Pokemon Berries.
        - Live on: https://lawrencesetien.pythonanywhere.com/allBerryStats
    - **GET /histogram**: This endpoint returns a plain HTML image of an Histogram of the frequency_growth_time variable.
        - Live on: https://lawrencesetien.pythonanywhere.com/histogram
