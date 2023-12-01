==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:


|   .
|   ├── Autos/
|   │   ├── __init__.py
|   │   └── example_auto.py
|   ├── oi/
|   │   ├── Keymap.py
|   │   └── OI.py
|   ├── Commands/
|   │   ├── __init__.py
|   │   └── example_command.py
|   ├── Subsystems/
|   │   ├── __init__.py
|   │   └── example_subsystem.py
|   ├── Sensors/
|   │   ├── __init__.py
|   │   └── example_sensor.py
|   ├── Utils/
|   │   └── example_function.py
|   ├── Units/
|   │   ├── __init__.py
|   │   └── SI.py
|   ├── Tests/
|   │   ├── Utils/
|   │   │   └── test_example_function.py
|   │   ├── subsystems/
|   │   │   └── test_example_subsystem.py
|   │   ├── Commands/
|   │   │   └── test_example_command.py
|   │   └── sensors/
|   │       └── test_example_sensor.py
|   ├── constants.py
|   ├── config.py
|   ├── robot_systems.py
|   └── robot.py

...yeah, that's a lot of stuff. Let's break it down.

Core Folders
------------

::
    .
    ├── Commands/
    │   ├── __init__.py
    │   └── example_command.py
    ├── Subsystems/
    │   ├── __init__.py
    │   └── example_subsystem.py
    ├── Sensors/
    │   ├── __init__.py
    │   └── example_sensor.py

.. graphviz:: 

    digraph {
        "Subsystem" -> "Command";
        "Sensor" -> "Command";
    }
