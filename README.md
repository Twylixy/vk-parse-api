## Install dependencies
It's highly recommended to use Poetry as package manager for that code, but you, probably, can use default pip. But, if you're using pip there is no guarantee that everything will be fine.

If you're installing dependencies with pip it is highly recommended to use Virtual Environment for your Python.
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate  # on Linux
$ ./.venv/Scripts/Activate.ps1  # on Windows (PowerShell)
$ poetry shell # with poetry
```

Then install dependencies
```bash
$ poetry install --no-root  # with Poetry
$ pip3 install -r requirements.txt  # with pip
```

## Run
Before execute verify, that you created **.env** based on **.env.example**.

```bash
python -m app
```

## Tests
Run within virtual environment
```bash
$ pytest
```