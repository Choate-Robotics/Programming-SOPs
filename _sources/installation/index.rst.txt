============
installation
============

Windows:
========

1. Install Python (http://www.python.org/download/)
    a. Make sure to check the box to add Python to your PATH

2. Verify Python is installed by opening a command prompt and typing `python`

3. Install Poetry by opening a powershell prompt and typing `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -`

Mac:
====

1. Install Rosetta 2 by opening a terminal and typing `softwareupdate --install-rosetta`

2. Install Homebrew by opening a terminal and typing `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

3. Install Python by opening a terminal and typing `brew install python`

4. Verify Python is installed by closing and opening the terminal and typing `python`

5. Install Poetry by opening a terminal and typing `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
    a. ..Important: if you get an error concerning [SSL: CERTIFICATE_VERIFY_FAILED], run `open /Applications/Python\ 3.9/Install\ Certificates.command` and try again

Linux:
======

1. Install Python by opening a terminal and typing `sudo apt-get install python3.9`

2. Verify Python is installed by closing and opening the terminal and typing `python`

3. Install Poetry by opening a terminal and typing `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

4. Verify Poetry is installed by closing and opening the terminal and typing `poetry`

============