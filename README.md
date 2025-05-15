# IESopt Project Template

This allows setting up pre-defined project structures for IESopt projects.

> [!IMPORTANT]
> This requires that `git` and `uv` are installed on your system. Consult the installation instructions for [uv](https://docs.astral.sh/uv/getting-started/installation/) or [git](https://git-scm.com/downloads/) if you don't have them installed yet.

## Using this template

> [!CAUTION]
> If you are using Windows, make sure to carefully read the specific instructions below before executing anything!

### Instructions for Windows users

1. You need to execute the command in your `Git Bash`. Do so by right-clicking inside your `dev` folder (the one where you keep all your projects) and selecting `Open Git Bash here`.
2. You most likely cannot copy-paste there; you can either right click into the shell and paste via the context menu, or try `Shift+Ins`.
3. If a popup opens during the setup process asking you which program to use to open some file, please select `Git Bash` and confirm your choice.
4. If it "randomly" launches VSCode and opens a `.sh` file, please follow the instructions below (in the _"Explanations & Problems"_ section) to fix this issue (which occurs if you've set VSCode as default choice for `.sh` files).

Now you should be ready to follow the actual instructions below.

### Creating a new project

Execute the following command in a terminal to create a new project (inside the current working directory) using this template

```bash
uvx cookiecutter gh:ait-energy/iesopt-project-template
```

and answer the questions in the terminal. For example, if you execute the command in `C:\Users\username\dev`, the new project will automatically be created in `C:\Users\username\dev\your_project_name`.

## Explanations & Problems

#### Why does it ask for my name / an author?

> This is used to set the author of the project. It is usually your name, but it can be anything you want. This is a part of the standardized `pyproject.toml` file, which controls your environment.

#### What is the project slug?

> This is a short abbreviation of the project name, that is used in a few places where spaces, etc., are not allowed. It is usually the same as the project name, but with spaces replaced by underscores and all letters in lowercase.

#### How can I accept default values?

> Every question ends in a `(something written here)`, which is the default value. If you want to accept the default value, just press `Enter` without typing anything.

#### What if it opens a weird `.sh` file in VSCode (or any other editor)?

> Open the file location of the `.sh` file that VSCode opened, then right-click it, select `Open with...`, then `Choose another app`, and then select `Git Bash`. Make sure to check the box that says `Always use this app to open .sh files` and then click `OK`. This will make sure that `.sh` files are opened with `Git Bash` in the future. After that, remove the folder and start from scratch. This time, it should work without any issues.

## Connecting to a remote repository

If you want to connect your local project to a remote repository, you can do so by executing the following command in the terminal:

```bash
git remote add origin <your-repo-url>
git push -u origin main
```

This can be used to push your local contents, e.g., to an internal/private GitLab repository. `<your-repo-url>` should be replaced with the URL of your remote repository (= _"the one that you would normally use to clone from"_).

## Remarks

The template contains various `.gitkeep` files, which are used to keep empty directories in the repository. These files are not necessary for the project and can be removed if desired.
