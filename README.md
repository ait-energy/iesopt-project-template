# IESopt Project Template

This allows setting up pre-defined project structures for IESopt projects.

## Using this template

> [!IMPORTANT]
> This requires that `git` and `uv` are installed on your system. Consult the installation instructions for [uv](https://docs.astral.sh/uv/getting-started/installation/) or [git](https://git-scm.com/downloads/windows) if you don't have them installed yet.

Execute the following command in a terminal to create a new project (inside the current working directory) using this template

```bash
uvx cookiecutter gh:ait-energy/iesopt-project-template
```

and answer the questions in the terminal. For example, if you execute the command in `C:\Users\username\dev`, the new project will automatically be created in `C:\Users\username\dev\your_project_name`.

> [!CAUTION]
> If you are using Windows, make sure to execute the above command in your `Git Bash`, by right-clicking inside your `dev` folder and selecting `Open Git Bash here`. Then just copy-paste (`Ctrl+V` might not work, you can always right click to paste via the context menu, or try `Shift+Ins`, in the `Git Bash`) the command above and hit `Enter`.

## Connecting to a remote repository

If you want to connect your local project to a remote repository, you can do so by executing the following command in the terminal:

```bash
git remote add origin <your-repo-url>
git push -u origin main
```

This can be used to push your local contents, e.g., to an internal/private GitLab repository. `<your-repo-url>` should be replaced with the URL of your remote repository ("the one that you would normally use to clone from").

## Remarks

The template contains various `.gitkeep` files, which are used to keep empty directories in the repository. These files are not necessary for the project and can be removed if desired.
