# {{ cookiecutter.project_name }}

## Description

{{ cookiecutter.short_description }}

## Setup

To setup this project, create a new envionment and install all dependencies using the following commands:

```bash
conda create -n {{ cookiecutter.project_slug }} python=3.12 -y
conda activate {{ cookiecutter.project_slug }}

pip install poetry
poetry install --no-root
```

## Usage

Make sure you have activated the environment `{{ cookiecutter.project_slug }}`, and then execute the code in `main.py`.

> **Remember:** The first time you execute the `import iesopt` statement, `iesopt` will download and setup the necessary Julia environment, which includes precompiling all dependencies. This process may take a few minutes, but is only required once.
