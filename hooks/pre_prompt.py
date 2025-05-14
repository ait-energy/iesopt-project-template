import sys
import subprocess


def is_uv_installed() -> bool:
    try:
        subprocess.run(["uv", "--version"], capture_output=True, check=True)
        subprocess.run(["uvx", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        print("ERROR: `uv` is not properly installed.")
        return False


def is_git_installed() -> bool:
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        print("ERROR: `git` is not properly installed.")
        return False


if __name__ == "__main__":
    if not (is_uv_installed() and is_git_installed()):
        sys.exit(1)
