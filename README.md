# Getting Started with Flask

## Setting up the project environment

If you don't already have it, install Python version 3 or above here: https://www.python.org/downloads/

Using a virtual environment is always a good practice as it keeps your project dependencies cleanly managed, segregated from the global Python modules. However, after Python 3 the virtual environment is built into python and does not need to be manually installed.

## Create a new directory for the project:
### `mkdir my-flask-application`
### `cd my-flask-application`

## Create a new virtual environment and activate it:
### `python -m venv env`
Activate it:
### `env\scripts\activate`

## Install Flask:
### `pip install Flask`

Now create a .py file and write some code.

## Run the Flask application:
### `python app.py`

You can now view the application at localhost:5000.

# Installing this template

To install this template all you need to do is clone the repo, navigate to the project folder, and install Flask there:

### `pip install Flask`

Flask may already be installed which is still fine. If this results in an error that looks something like this:

 WARNING: Failed to write executable - trying to use .deleteme logic
 ERROR: Could not install packages due to an OSError: [WinError 2] The system cannot find the file specified: 'c:\\python39\\Scripts\\flask.exe' -> 'c:\\python39\\Scripts\\flask.exe.deleteme'

 Try running the application anyway. This is not a critical error.

 Run the application:

### `python app.py` 



