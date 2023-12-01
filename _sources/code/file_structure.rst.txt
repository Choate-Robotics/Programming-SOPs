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
|   │       └── test_example_sensor.py
|   ├── constants.py
|   ├── config.py
|   ├── robot_systems.py
|   └── robot.py

.. graphviz:: 

    digraph {
        'auto/';
        'oi/';
        'commands/';
        'subsystems/';
        'sensors/';
        'utils/';
        'units/';
        'tests/';
        'constants.py';
        'config.py';
        'robot_systems.py';
        'robot.py';
    }

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

Flow
----

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
