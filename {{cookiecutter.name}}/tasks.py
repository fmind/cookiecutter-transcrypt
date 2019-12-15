"""Tasks of the project."""

from pathlib import Path

from invoke import task


@task
def venv(c, force=False):
    """Create a virtual environment."""
    if not Path("venv").exists() or force:
        c.run("python3 -m venv venv --clear")
        c.run("venv/bin/pip install -r requirements.txt")


@task(venv)
def serve(c):
    """Serve the web application."""
    c.run("venv/bin/python3 -m http.server")


@task(venv)
def transpile(c):
    """Transpile the application."""
    c.run("venv/bin/transcrypt app.py")
