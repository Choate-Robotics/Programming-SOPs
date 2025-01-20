==================
7407 Code Style
==================

Docstrings
----------

We find everyone has slight differences in how they do docstrings.

If the method is decently self explanatory, then something like the following is fine:

.. code-block:: python
    def func2():
        """
        Summary of the function.

        """

If the method is more complex with inputs and outputs:

.. code-block:: python
    def func2(param1, param2):
        """
        Summary of the function.

        Description of the function's purpose and behavior, explaining
        any non-obvious logic.

        Args:
            param1 (type): Description of param1.
            param2 (type): Description of param2.

        Returns:
            return_type: Description of the return value.
        """


Comments
--------

We typically like to add a space after the # and capitalize.

.. code-block:: python
    # This is a comment

instead of

.. code-block:: python
    #this is a comment

