==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:

.
├── autos/
│   ├── __init__.py
│   └── example_auto.py
├── oi/
│   ├── Keymap.py
│   └── OI.py
├── commands/
│   ├── __init__.py
│   └── example_command.py
├── subsystems/
│   ├── __init__.py
│   └── example_subsystem.py
├── sensors/
│   ├── __init__.py
│   └── example_sensor.py
├── utils/
│   ├── __init__.py
│   └── example_function.py
├── units/
│   ├── __init__.py
│   └── SI.py
├── tests/
│   ├── utils/
│   │   └── test_example_function.py
│   ├── subsystems/
│   │   └── test_example_subsystem.py
│   ├── commands/
│   │   └── test_example_command.py
│   └── sensors/
│       └── test_example_sensor.py
├── .deploy_cfg
├── constants.py
├── config.py
├── robot_systems.py
└── robot.py


...yeah, that's a lot of stuff. Let's break it down.

Core Folders
------------

.
├── commands/
│   ├── __init__.py
│   └── example_command.py
├── subsystems/
│   ├── __init__.py
│   └── example_subsystem.py
├── sensors/
│   ├── __init__.py
│   └── example_sensor.py


.. graphviz:: 

    digraph {
        "Subsystem" -> "Command";
        "Sensor" -> "Command";
    }
