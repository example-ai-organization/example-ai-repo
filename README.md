# example-ai-repo

An example of a repository to demonstrate the use of Github projects (and Poetry as a package manager).

## How to run

First, you must install poetry. Use [this guide](https://python-poetry.org/docs/#installing-with-pipx) to help you install poetry in your machine.

Then, move to the project's root directory (where the .toml file is located) and type:

```sh
poetry install
```

This will automatically setup a virtual environment for you and download the required packages for this project.

Then, add a `.env` file to the root directory with the following entry: `GOOGLE_API_KEY=your-api-key`. You can sign up for a free API key from Google AI (gemini).

Finally, simply execute the shell script `start_ui.sh` using the following command:

```sh
poetry run start_ui.sh
```

This starts a local streamlit server. We use the `poetry` command to ensure that we're running the script in the virtual environment that was created. That's because the shell script depends on a package that was installed in the virtual environment.

![streamlit basic ui](images/streamlit_ui_basic.png)

To exit the server you started, click **CTRL+C** in your shell.

_Tip_: Your IDE (like VS Code) might not be using the virtual environment that Poetry had created, so if you open one of the Python files in this project, it can tell you that some Python packages are missing. If you're using VS Code, you can `Select Interpeter` using the command palette, and change to the virtual environment that Poetry had created for you. This can also help you start terminals in your virtual environment.
