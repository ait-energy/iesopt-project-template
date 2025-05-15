#!/bin/bash

if [ "{{ cookiecutter.iesopt_version }}" == "latest" ]; then
    uv add iesopt
else
    uv add iesopt=={{ cookiecutter.iesopt_version }}
fi

uv add pandas

uv sync

git init --initial-branch=main
git add .
git commit --message "chore(cookiecutter): initial commit" --quiet

uv tool install pre-commit --with pre-commit-uv
uv tool run pre-commit install

uv run python -c "import iesopt"

git add .
git commit --message "chore(cookiecutter): initialize pre-commit and iesopt dependencies" --quiet

echo "IESopt project template setup complete!"
echo ""
echo "Consider adding a remote repository and pushing your changes:"
echo "  1. git remote add origin <your-repo-url>"
echo "  2. git push -u origin main"
