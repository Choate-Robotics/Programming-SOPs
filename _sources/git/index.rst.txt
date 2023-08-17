==============
Git and Github
==============

What is it?
-----------

Git is a version control system. It allows you to keep track of changes to a project over time. It also allows you to collaborate with others on a project.

.. hint:: 

    * Think of it as a google doc for code with a few exceptions:
        * You have to manually save your changes. **This is called a commit.**
        * You have to manually sync your changes with the server. **This is called a push.**
        * You can't see other people's changes until they sync them with the server. **This is called a pull.**

    .. note::
        Why is git more limiting than google docs? In simple terms, security. If changes save and sync automatically, potentially breaking code would be released to the repository. Thats why you have to manually commit and push your changes. This allows you to make sure that your code is working before you release it to the repository. It also allows you to make sure that you don't overwrite other people's changes.

    * Now take that google doc and imagine that you can see every change that has ever been made to it. You can see who made the change, when they made it, and what they changed. You can also revert back to any previous version of the document. **This is the Git commit history.**

    * Now imagine that you can make a copy of the document, make changes to it, and then merge those changes back into the original document. You can also merge changes from other people's copies of the document into your copy. **This is branching and merging.**

    * If you are interested in learning more, check out the `Git Book <https://git-scm.com/book/en/v2>`_.

How does our team use it?
-------------------------

We use Git to keep track of changes to our code with branches

we have three main branches in every repository:

* **Main (master):** this is the clean code that has been tested. One that you can bet your life on. This is the code that we base our competition code on.
* **Dev:** this is the code that we are currently working on. It is not guaranteed to work, but it should be close. This is the code that we base our practice code on. This is also for testing new features in conjunction with each other.
* **Feat/#feature_name#:** this is the code for a specific feature. It is not guaranteed to work. This is for adding and testing new features individually.

What code do we run during competitions?

* We make branches for each competition, which are based off of the Main branch. This is so we can edit based on the competition deviances without affecting the main code. We then merge files we like from the competition branch into the main branch after the competition.
* **Comp/#competition_name#:** as an example, we would have a branch called Comp/Worlds.

Other branches:

* **Hotfix/#hotfix_name#:** this is for fixing bugs in the main branch. It is based off of the main branch and is merged back into the main branch after the bug is fixed.


How do I use it?
----------------

There are two ways to use Git. You can use it from the command line or you can use a GUI. The GUI is easier to use, but the command line is more powerful. 

.. note:: 
    both methods utilize the same commands, meaning switching from one to another is not too challenging. The GUI just makes it easier to visualize what is happening.


.. tab-set::

    .. tab-item:: GUI


        Github Desktop is a GUI for Git. It makes it easy to see what changes you have made and to sync them with the server. It also makes it easy to create branches and merge them back into the main branch.

        .. note::
            You can download Github Desktop `here <https://desktop.github.com/>`_.

        for information on how to use Github Desktop, check out the `Github Desktop Guide <https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop>`_.

    .. tab-item:: CLI

        The command line is a text based interface to your computer. It is a powerful tool that allows you to do many things that you can't do with a GUI. It is also a bit more complicated to use, since you have to remember the commands.

        .. note:: 
            If you are using a Mac, you can open the terminal by pressing command + space and typing terminal. If you are using Windows, you can open the command prompt by pressing the windows key and typing cmd.

        .. dropdown:: Basic Commands for Navigation and File Management

            * ``cd`` - change directory

            * ``cd..`` - go up one directory

            * ``dir`` - list files in current directory

            * ``mkdir`` - make directory

            * ``rmdir`` - remove directory

            * ``del`` - delete file
        
        Here are some basic commands to get you started:

        .. code-block:: bash

            # clone a repository to the current directory
            git clone #repository_url

            # check the status of your repository
            git status

            # add a file to the staging area
            git add #file_name

            # commit your changes
            git commit

            # push your changes to the server
            git push

            # pull changes from the server
            git pull

            # create a new branch
            git branch

            # switch to a different branch
            git checkout #branch_name

            # merge a branch into the current branch
            git merge #branch_name

            # delete a branch
            git branch -d #branch_name

        .. note::
            If you are interested in learning more, check out the `Git Book <https://git-scm.com/book/en/v2>`_.





 

