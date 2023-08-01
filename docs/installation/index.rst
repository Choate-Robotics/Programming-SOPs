============
Installation
============

.. contents:: Table of Contents
   :local:
   :depth: 2

This document describes the necessary installations to effectively run code in this organization.

Software
========

.. tabset::

    .. tabitem:: Windows
    :sync: Win

        1. Install Python (http://www.python.org/download/)
            .. caution::

                Make sure to check the box that says "Add Python to PATH", otherwise you will have to add it manually. Thats not fun.

        2. Verify Python is installed by opening a command prompt and typing 
            ..  code-block:: python

                python

        3. Install Poetry by opening a powershell prompt and typing 

            ..  code-block:: powershell

                (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -



    .. tabitem:: Mac
    :sync: Mac

        1. Install Rosetta 2 by opening a terminal and typing
            .. code-block:: bash

                softwareupdate --install-rosetta

        2. Install Homebrew by opening a terminal and typing 

            .. code-block:: bash

                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

        3. Install Python by opening a terminal and typing 

            .. code-block:: bash

                brew install python

        4. Verify Python is installed by closing and opening the terminal and typing 
            
            .. code-block:: bash

                python

        5. Install Poetry by opening a terminal and typing 
                
            .. code-block:: bash

                curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
            
            .. important::

                if you get an error concerning ``[SSL: CERTIFICATE_VERIFY_FAILED]``, run ``open /Applications/Python\ 3.9/Install\ Certificates.command`` and try again

    .. tabitem:: Linux
    :sync: Linux

        1. Install Python by opening a terminal and typing 

            .. code-block:: bash

                sudo apt-get install python3.9

        2. Verify Python is installed by closing and opening the terminal and typing 

            .. code-block:: bash

                python

        3. Install Poetry by opening a terminal and typing 

            .. code-block:: bash

                curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

        4. Verify Poetry is installed by closing and opening the terminal and typing 

            .. code-block:: bash

                poetry

IDE
===

What is an IDE?
---------------
* IDE stands for Integrated Development Environment.
* An IDE is a program that is used to write code.
---------------

There are many IDEs that can be used to develop Python code.  The following are recommended:

VSCode
------
* The most popular IDE for our team.
* free and open source, and has a large community of developers.
* general purpose IDE that can be used for many different languages.
* very customizable and has a large number of extensions that can be used to add functionality.
* can be downloaded from (https://code.visualstudio.com/)

PyCharm
-------
* A very popular IDE for Python development.
* free and open source, and has a large community of developers.
* has a free community edition and a paid professional edition.
* More focused on Python development than VsCode.
* can be downloaded from (https://www.jetbrains.com/pycharm/)

Vim
---
* Try if you dare.
* can be downloaded from (https://www.vim.org/download.php)
* how do i exit vim? Please help me.


Github
======
* Github is a website that hosts git repositories.
* We use Github to host our code and to collaborate with other developers.
* Github can be accessed at (github.com/Choate-Robotics)
.. important::

    Github is not the same as git.  Git is a version control system that is used to manage code.  Github is a website that hosts git repositories.
.. note::

    You will need to create a Github account to access our repositories. Let the current team leader know your Github username so you can be added to the organization.

**How to Install Git**
----------------------

1. Download Git from (https://git-scm.com/downloads)

2. Run the installer

3. Verify Git is installed by opening a command prompt and typing 
    
    .. code-block:: bash

        git

.. tip::

    **Github Desktop**
    * Github Desktop is a GUI for git that makes it easier to use.

    1. Download Github Desktop from (https://desktop.github.com/)

    2. Run the installer

    3. Open Github Desktop and sign in with your Github account
