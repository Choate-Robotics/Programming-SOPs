Poetry
======

What is it?
-----------

* Poetry is a tool for dependency management and packaging in Python with a virtual environment.

.. note:: 
    * dependencies are libraries that your project depends on. For example, if you are using the requests library, then requests is a dependency of your project.
    * a virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. Different virtual environments can have different versions of Python, and can have different sets of installed packages. Think of it as a standalone machine in simple terms.  

* It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.
* Runs inside a virtual environment, so you don't need to manage your own virtual environment.

Why use it?
-----------

* "I don't know why its not working, it runs on my machine!"

* It allows us to share code with others without worrying about library versions, since poetry will handle that for us.

* It allows us to easily install our dependencies on a new machine.

* Since it runs inside a virtual environment, it doesn't pollute our global python environment.

* It will work on every ones computer, since we are all using the same virtual environment.

How to use it?
--------------

.. note:: 
    You will need to install Poetry on your machine first.
    If you have not done so, refer to the ::doc:`/installation/index` page for instructions on how to install Poetry.

Setup:
~~~~~~

1. Create a new project folder, or navigate to an existing project folder.
2. In the terminal, run the command ``poetry init``. This will create a new poetry project.
3. The terminal will ask you a series of questions about your project configuration. You can skip most of them by pressing enter.
4. Once you have finished, you should see a new file called ``pyproject.toml``. This is the configuration file for your project.

Adding dependencies:
~~~~~~~~~~~~~~~~~~~~

1. to add dependencies, run the command ``poetry add <dependency>``. For example, ``poetry add numpy`` will add the numpy library to your project.
2. to install all dependencies, run the command ``poetry install``. This will install all dependencies in your project. This will also create a virtual environment for your project.
3. use ``poetry lock`` to update the ``poetry.lock`` file. This file contains the exact versions of the dependencies that you are using. This is useful for sharing your project with others.

Running your project:
~~~~~~~~~~~~~~~~~~~~~

1. to run your project, use ``poetry run <command>``. For example, ``poetry run python main.py`` will run the ``main.py`` file in your project. this will run the file inside the virtual environment, so you don't need to worry about installing the dependencies with pip (though its recommended since autocompletion will not work on IDEs).
2. to open a shell inside the virtual environment, use ``poetry shell``. This will open a shell inside the virtual environment, so you can run commands without using ``poetry run``. To exit the shell, use ``exit``.

.. note:: 
    a shell is a command line interface that allows you to run commands on your computer. For example, the terminal is a shell. by opening a shell inside the virtual environment, you can run commands without using ``poetry run``.