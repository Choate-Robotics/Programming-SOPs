Testing Code
============

Unit testing
------------

Testing code is an important part of the development process. As you make code, you revise and revise it.
As you make changes in the code, you can introduce revisions that have negative effects on the code in unexpected ways.
Writing and running tests are ways to ensure that as you update and improve your code, you maintain functionality
that you understand and that works as intended.

Writing Tests for FRC Robots
----------------------------

Check out:

`RobotPy Testing Guide <https://robotpy.readthedocs.io/en/stable/guide/testing.html>`_

To start writing tests for the code, use the repository linked below,
and make sure that you have set up the proper libraries.

Starter Code
^^^^^^^^^^^^

You can find starter code for this project here: `DriveStraight2024 <https://github.com/mbardoeChoate/DriveStraight2024>`_

The starter code contains three files: ``robot.py``, ``subsystems/drivetrain.py``, and ``pyproject.toml``.
You may need to set up the project to be a RobotPy project. Use the following commands:

.. code-block:: shell

    python3 -m pip install robotpy
    python3 -m robotpy init
    python3 -m robotpy sync

To run the tests, type the following into the terminal:

.. code-block:: python

    python3 -m robotpy test

This command creates a ``tests`` folder and adds some basic tests to ensure that
the code runs in autonomous and teleoperated modes without errors. This allows you
to test your code without running the robot.

How to Write Tests
------------------

When writing a test, there are a few things to keep in mind:

- Organize your tests in the same way you organize your robot's code.
- Place tests for one file primarily in a single test file.

ArcadeDrive Test
^^^^^^^^^^^^^^^^

At the top of the file, include necessary imports. For example, we will use the ``pytest`` library and sometimes the ``unittest.mock`` library.

Create a Python file called ``test_drivetrain.py`` in a ``tests`` directory:

.. code-block:: python

    import pytest
    from drivetrain import Drivetrain

When writing tests:

- The filename must include the word ``test`` so the testing library recognizes it as a test file.
- Method names should start with ``test`` to indicate they are test methods.

Example test for ``arcadeDrive``:

.. code-block:: python

    def test_arcadeDrive():
        # Setup the test
        drivetrain = Drivetrain()
        drivetrain.drive = MagicMock()

        # Action
        drivetrain.arcadeDrive(0.2, 0.3)

        # Assert
        drivetrain.drive.arcadeDrive.assert_called_once_with(0.3, 0.2)

Each test includes three parts:

1. **Setup**: Create objects and prepare for the test.
2. **Action**: Call the method being tested.
3. **Assert**: Verify the results.

Testing Resetting Encoders
^^^^^^^^^^^^^^^^^^^^^^^^^^

Mocking
-------

The ``MagicMock`` object is a tool for creating fake objects used in tests. It tracks method calls and arguments passed.

Example of mocking dependencies in the ``Drivetrain`` class:

.. code-block:: python

    @pytest.fixture
    def drivetrain() -> Drivetrain:
        # Create a drivetrain with mocked dependencies
        drive = Drivetrain()
        drive.left_motor = MagicMock()
        drive.right_motor = MagicMock()
        drive.leftEncoder = MagicMock()
        drive.rightEncoder = MagicMock()
        drive.drive = MagicMock()
        drive.gyro = MagicMock()
        return drive

Example test using the fixture:

.. code-block:: python

    def test_reset_encoders(drivetrain: Drivetrain):
        '''A test to ensure that resetting the encoders resets all encoders.'''
        # Setup
        left_reset = drivetrain.leftEncoder.reset
        right_reset = drivetrain.rightEncoder.reset

        # Action
        drivetrain.resetEncoders()

        # Assert
        left_reset.assert_called_once()
        right_reset.assert_called_once()

For more details on assert methods, visit the `unittest.mock documentation <https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called>`_.

Monkeypatching
--------------

Monkeypatching allows you to override functions during tests. Example:

.. code-block:: python

    def test_averageDistanceMeter(drivetrain: Drivetrain, monkeypatch) -> None:
        # Setup
        def mock_getRightDistanceInch(self):
            return 3.0

        def mock_getLeftDistanceInch(self):
            return 2.0

        monkeypatch.setattr(Drivetrain, "getLeftDistanceInch", mock_getLeftDistanceInch)
        monkeypatch.setattr(Drivetrain, "getRightDistanceInch", mock_getRightDistanceInch)

        # Action
        dist = drivetrain.getAverageDistanceInch()

        # Assert
        assert dist == 2.5

Parameterizing
--------------

Use parameterization to test with multiple input values. Add a decorator:

.. code-block:: python

    @pytest.mark.parametrize(('left_Distance', 'right_Distance', 'output'), [
        (2, 3, 2.5),
        (10, 20, 15),
        (-3, 3, 0),
    ])
    def test_averageDistanceMeter(drivetrain: Drivetrain, monkeypatch, left_Distance,
                                  right_Distance, output) -> None:
        # Setup
        def mock_getRightDistanceInch(self):
            return right_Distance

        def mock_getLeftDistanceInch(self):
            return left_Distance

        monkeypatch.setattr(Drivetrain, "getLeftDistanceInch", mock_getLeftDistanceInch)
        monkeypatch.setattr(Drivetrain, "getRightDistanceInch", mock_getRightDistanceInch)

        # Action
        dist = drivetrain.getAverageDistanceInch()

        # Assert
        assert dist == output


Running Tests
-------------

To run the tests, type the following into the terminal:

.. code-block:: python

    python3 -m robotpy test

This command runs all the tests in the ``tests`` directory.
If a test fails, the command will output the error message, and you can debug the issue. It will give you information
about the test that failed and the line number where the failure occurred, as well as what the inputs were, and generally
what the expected output was as well as the actual output generated.