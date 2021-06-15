import subprocess
import importlib


def get_git_revision():
    return (
        subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
        .decode("utf-8")
        .strip()
    )


def get_semantic_version():
    return (
        subprocess.check_output(["poetry", "version", "--short"])
        .decode("utf-8")
        .strip()
    )
