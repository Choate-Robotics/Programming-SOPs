====================
robotpy-toolkit-7407
====================

This is a collection of tools that are useful for FRC teams using RobotPy. This library cuts down on the boilerplate that is required to write RobotPy code. 
This also contains our own custom wrappers for the WPILib classes that we use, as well as some other useful classes, like Swerve Drive and PID Controllers.

Installation
------------
To install this library on your computer, run the following command:

.. code-block:: bash

    pip install robotpy-toolkit-7407

.. note::

    robotpy-toolkit-7407 is already inside the poetry project, so you don't necessarily need to install it on your computer.
    It is recommended, however, since the autocompletion for IDE's will work.

    * for more information about poetry, visit our :doc: `poetry documentation <poetry/index>`
  
Usage
-----

* `RobotPy Documentation <https://choate-robotics.github.io/7407-RobotPy-Toolkit/#>`_

* Simply import the necessary classes from the library into your code:

.. code-block:: python
    :linenos:

    from robotpy_toolkit.sensors import limelight

    limelight = limelight.Limelight()


