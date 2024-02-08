# Cloning this repository

# Git Installation and Repository Cloning

Follow these steps to install Git, clone the repository where this Markdown file is present, and get started with version control.

## Step 1: Install Git

If you don't have Git installed, download and install it from the [official Git website](https://git-scm.com/).

## Step 2: Open a Terminal or Command Prompt

Open your terminal or command prompt where you want to clone the repository.

## Step 3: Clone the Repository

Use the following command to clone the repository:

`git clone <repository_url>`


# Setting up a Python 3.10 Virtual Environment

Follow these steps to create a Python virtual environment and install dependencies from the `requirements.txt` file.

## Step 1: Install Python 3.10

Ensure that you have Python 3.10 installed on your system. You can download it from [the official Python website](https://www.python.org/downloads/).

### For Windows

For further ease, [add the installed python to the PATH environment variable](https://datatofish.com/add-python-to-windows-path/) if it is not already present.

*To verify, run `python --version` in terminal. If it is present in PATH, it should return the version of python with no error.*

## Step 2: Open a Terminal or Command Prompt

Open your terminal or command prompt where you want to create the virtual environment.

## Step 3: Create a Virtual Environment

Run the command `python -m venv egd-env`

## Step 4: Activate the virtual environment

### For Windows:

If using command prompt, in the root directory of egd-env, run `egd-env/Scripts/activate.bat`
If using powershell (recommended), run `egd-env/Scripts/activate.ps1`

### For MacOS:

Run `source egd-env/bin/activate`

*To deactivate the environment, simply run `deactivate`*

## Step 5: Install Dependencies from 'requirements.txt'

After activating the virtual environment, run the command `pip install -r requirements.txt`

Verify installation by running `pip list` to display the list of installed packages.

