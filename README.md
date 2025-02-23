# Instructions
1. Copy and rename `example.env` to `.env`
```sh
cp example.env .env
```

2. Update `PROJECT_PATH` in the `.env` to point where your project is.
Note: This is required to execute the tests.

3. Install the app:
```sh
bash install.sh
```

4. Run tests:
```sh
bash run_tests.sh
```

# TODO
- [x] Create an overview structure of the project.
- [x] Start flask with basic API.
- [x] Dockerize flask app.
- [x] Config debug mode.
- [x] Get data from Poke API.
- [x] Improve API.
- [ ] Write instructions:
    - [ ] Install docker and start venv?
    - [ ] Run docker compose file.
    - [ ] Run tests.
    - ...

Others:
- [x] Add unit tests
- [x] Add smoke tests
- [ ] ...