# Python Tkinter CRUD Example

This is a project for a small university homework.
Although the UX is pretty outdated, it was a pretty good exercice to get familiar with Tkinter and how to communicate with a MySQL database in Python3.

Note that tthe application is documented throughout the files in the [src directory](src). In addition, `pylint` was used for cleaner code.

![app-image](media/screenshot.JPG)

## Getting started

1. Install the dependencies with

```
pip install -r requirements.txt
```

2. Initialize the database (no ORM yet)

   - For that, you have to run the [`init.sql`](init.sql) against a MySQL or a MariaDB database.
   - Create a `.env` from the [`.env.example`](.env.example) file and edit it if needed.

3. Run the app with

```
python main.py
```

## Developing with Virtualenv

1. Initializing the project (once initially)

```bash
virtualenv .
```

2. Entering the virtual environment

```bash
source bin/activate
# or if on windows
source Scripts/activate
```

3. Installing packages

```bash
pip install <my-package>
```

1. Writing the requirements

```bash
pip freeze > requirements.txt
```

4. Exiting the virtual environment

```bash
deactivate
```

### Resources

- [Setting up virtualenv](https://realpython.com/python-virtual-environments-a-primer/)
