# allure-steplog-example

Tests example with allure and pytest where every allure step logs captured and attached to report.

## Install

* Using poetry:
```shell
$ poetry install
```

* Using pip:
```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install .
```

## Run tests

Run pytest command:
```shell
(.venv) $ pytest tests
```

## Generate allure report

Build image with allure commandline:
```shell
$ docker build . -t allure
```

Generate allure report:
```shell
$ docker run -ti --rm -p 8080:8080 -v $(pwd):/app:Z allure generate
```

Open allure report:
```shell
$ docker run -ti --rm -p 8080:8080 -v $(pwd):/app:Z allure open -h 0.0.0.0 -p 8080
```

Example allure report:

![Example allure report](report.png)
