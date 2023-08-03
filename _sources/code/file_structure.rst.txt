==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:

.. graphviz::


    digraph file_structure {

        subgraph OI {
            label="OI/"
            Keymap -> OI_py
        }

        subgraph tests {
            label="tests/"
            tests_subsystems -> tests
            tests_commands -> tests
            tests_sensors -> tests
        }

        node [shape=box]
        commands [label="commands/"]
        subsystems [label="subsystems/"]
        OI [label="OI/"]
        OI_py [label="OI/OI.py"]
        Keymap [label="OI/Keymap.py"]
        sensors [label="sensors/"]
        tests [label="tests/"]
        tests_subsystems [label="tests/subsystems/"]
        tests_commands [label="tests/commands/"]
        tests_sensors [label="tests/sensors/"]
        utils [label="utils/"]
        robot_py [label="robot.py"]
        constants_py [label="constants.py"]
        config_py [label="config.py"]
        robot_systems_py [label="robot_systems.py"]

        commands -> robot_py
        commands -> OI_py
        OI -> robot_py
        constants_py -> robot_py
        constants_py -> subsystems
        constants_py -> sensors
        constants_py -> utils
        config_py -> subsystems
        config_py -> sensors
        subsystems -> robot_systems_py
        sensors -> robot_systems_py
        utils -> subsystems
        utils -> commands
        robot_systems_py -> robot_py
        subsystems -> tests
        subsystems -> commands
        commands -> tests
        sensors -> tests
        constants_py -> tests
        constants_py -> robot_py
    }