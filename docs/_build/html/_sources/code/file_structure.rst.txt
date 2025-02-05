==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:


|   root/
|   ├── autos/
|   │   ├── __init__.py
|   │   └── example_auto.py
|   ├── oi/
|   │   ├── Keymap.py
|   │   └── OI.py
|   ├── commands/
|   │   ├── __init__.py
|   │   └── example_command.py
|   ├── subsystems/
|   │   ├── __init__.py
|   │   └── example_subsystem.py
|   ├── sensors/
|   │   ├── __init__.py
|   │   └── example_sensor.py
|   ├── utils/
|   │   └── example_function.py
|   ├── units/
|   │   ├── __init__.py
|   │   └── SI.py
|   ├── tests/
|   │   ├── utils/
|   │   │   └── test_example_function.py
|   │   ├── subsystems/
|   │   │   └── test_example_subsystem.py
|   │   ├── commands/
|   │   │   └── test_example_command.py
|   │   └── sensors/
|   │   │   └── test_example_sensor.py
|   ├── constants.py
|   ├── config.py
|   ├── robot_systems.py
|   └── robot.py

Here is the flow:

.. graphviz:: 
    
    digraph {
        "Subsystem" -> "Command";
        "Sensor" -> "Command";
        "Util" -> "Command";
        "Subsystem" -> "robot_systems.py";
        "Sensor" -> "robot_systems.py";
        "Constant" -> "Subsystem";
        "Constant" -> "Sensor";
        "Constant" -> "Util";
        "Config" -> "Subsystem";
        "Config" -> "Sensor";
        "Config" -> "Util";
        "Keymap" -> "OI";
        "Command" -> "OI";
        "Command" -> "Robot"
        "OI" -> "Robot";
        "robot_systems.py" -> "Robot";

    }

...yeah, that's a lot of stuff. Let's break it down.

Core Folders
------------

Subsystems
~~~~~~~~~~

The subsystem folder contains all of the subsystem mechanisms for the robot. this includes the drivetrain, elevator, intake, etc.

Subsystem classes contain methods for controlling the subsystem, and are called by commands.

This class will initialize in the ``robot_systems.py`` file under the ``Robot`` class. This will allow the subsystems to be called by commands.

.. note:: 

    For example, a subsystem for the elevator could have the following methods:

    * ``move_to_height(height)`` - moves the elevator to a certain height
    * ``move_to_speed(speed)`` - moves the elevator at a certain speed
    * ``stop()`` - stops the elevator
    * ``get_height()`` - returns the height of the elevator
    * ``zero_elevator()`` - zeros the elevator encoder by sending the elevator to the bottom and resetting the encoder.
    * ``get_encoder()`` - returns the encoder value of the elevator

    These classes should be as simple as possible, and should not contain any logic. All logic should be contained in commands.

    Its also important to add in comments for each method, so that the code is easy to understand.

.. important::

    Most subsystems will contain the ``init()`` method. This method is called when the robot is initialized and recieving connection from devices
    under the CAN network. This method should be used to initialize encoders, motors, etc.

    
    This will be called in the ``RobotInit()`` method in ``robot.py`` using the ``robot_systems.py`` file.

    * If you don't initialize your motors in the ``init()`` method but at the top of the class, the robot will not work, and you will get errors or connection loss.
    
    Please please please put it in there for our sanity.


.. important:: 
    
    * All subsystems must inherit from the :class:`.Subsystem` class.
    * Subsystems are not running any logic whatsoever. They are simply a way to organize code in a clean manner.

Sensors
~~~~~~~

The sensor folder contains all of the sensors for the robot. This includes the gyro, encoders, etc.

Similar to the subsystems, sensor classes contain methods for getting data from the sensors, and are called by commands.

This class will initialize in the ``robot_systems.py`` file under the ``Sensor`` class. This will allow the sensors to be called by commands.

.. note:: 

    For example, a sensor for a limelight camera could have the following methods:

    * ``get_distance()`` - returns the distance from the limelight to the target
    * ``get_angle()`` - returns the angle from the limelight to the target
    * ``get_target()`` - returns whether or not the limelight has a target

    These classes should be as simple as possible, and should not contain any logic. All logic should be contained in commands.

Commands
~~~~~~~~

commands are the logic of the robot. They are called by the OI or the robot runtime, and call methods from subsystems and sensors.

There are many different ways to write a command, but the most common way is to use the ``initialize()``, ``execute()``, and ``isFinished()`` methods.

.. note:: 

    For example, a command for moving the elevator to a certain height could have the following methods:

    * ``initialize()`` - initializes the command
    * ``execute()`` - moves the elevator to the height
    * ``isFinished()`` - returns whether or not the elevator is at the height
    * ``end()`` - stops the elevator

    These methods should use the functions from the subsystems and sensors to control the robot.

    Its also important to add in comments for each method, so that the code is easy to understand.


Subsystem, Sensor, Command flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. graphviz:: 

    .. digraph {
        "Subsystem" -> "Command";
        "Sensor" -> "Command";

    }

This is the standard flow for a command. The command calls methods from the subsystems and sensors to control the robot.

Complementary Files and Folders
-------------------------------

utils
~~~~~

The utils folder contains cross-subsystem functions that are used by both subsystems and commands.

These functions are not bound to any class, and are not called in the ``robot_systems.py`` file.

.. note:: 
    
        For example, a function for converting inches to meters could be in the utils folder:
    
        * ``inches_to_meters(inches)`` - converts inches to meters
    
        These functions should be as simple as possible, and should not contain any logic. All logic should be contained in commands.

constants.py
~~~~~~~~~~~~

The constants file contains all of the physical constants for the robot 
(IE: variables that are in correlation with physical measurements, and therefore, not likely to change). 

Constants variables are used in the subsystems and sensors to control the robot.

Some examples of constants are:

* ``DRIVETRAIN_WHEEL_DIAMETER`` - the diameter of the drivetrain wheels

* ``ELEVATOR_MAX_HEIGHT`` - the maximum height of the elevator

* ``DRIVETRAIN_MAX_SPEED`` - the maximum speed of the drivetrain

* ``DRIVETRAIN_MAX_ACCELERATION`` - the maximum acceleration of the drivetrain

you get the idea.


config.py
~~~~~~~~~

The config file contains all of the configuration variables for the robot
(IE: variables that are not in correlation with physical measurements, which are more likely to change on the fly during events).

Config variables are used in the subsystems and sensors to control the robot.

Some examples of configuration variables are:

* ``ELEVATOR_MOTOR_ID`` - the CAN ID of the elevator motor

* ``ABSOLUTE_ENCODER_OFFSET`` - the offset of the absolute encoder

* ``ELEVATOR_ZERO_SPEED`` - the speed of the elevator when zeroing

* ``ELEVATOR_ACCELERATION`` - the acceleration of the elevator (This is not the same as the maximum acceleration of the elevator, in which case the elevator would physically break)

* ``SENSOR_DIO_PORT`` - the DIO port of the sensor

you get the idea.

Updated flow
~~~~~~~~~~~~

.. graphviz:: 

    digraph {
        "Subsystem" -> "Command";
        "Sensor" -> "Command";
        "Util" -> "Command";
        "constants.py" -> "Subsystem";
        "constants.py" -> "Sensor";
        "constants.py" -> "Util";
        "config.py" -> "Subsystem";
        "config.py" -> "Sensor";
        "config.py" -> "Util";
    }