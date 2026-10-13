venv := ".venv"
python := if os_family() == "windows" { venv / "Scripts" / "python.exe" } else { venv / "bin" / "python" }
set shell := ["bash", "-c"]

setup:
    @test -e "{{python}}" || python -m venv {{venv}}
    @"{{python}}" -m pip install -q -q -r requirements.txt flake8

lint: setup
    "{{python}}" -m flake8 .

run folder file="main": setup
    #!/usr/bin/env bash
    PY_PATH="{{folder}}/{{file}}.py"
    IPYNB_PATH="{{folder}}/{{file}}.ipynb"

    if [[ -f "$PY_PATH" ]]; then \
        PYTHONPATH=. "{{python}}" "$PY_PATH"; \
    elif [[ -f "$IPYNB_PATH" ]]; then \
        echo "This is a Jupyter Notebook ($IPYNB_PATH)"; \
    else \
        echo "Error: Neither $PY_PATH nor $IPYNB_PATH was found." >&2; \
        exit 1; \
    fi
    