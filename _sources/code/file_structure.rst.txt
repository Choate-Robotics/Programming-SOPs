==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:

.. graphviz::


    digraph file_structure {
        node [shape=box]
        commands [label="commands/"]
        subsystems [label="subsystems/"]
        OI [label="OI/"]
        sensors [label="sensors/"]
        tests [label="tests/"]
        utils [label="utils/"]
        robot_py [label="robot.py"]
        constants_py [label="constants.py"]
        config_py [label="config.py"]
        robot_systems_py [label="robot_systems.py"]

        commands -> robot_py
        commands -> OI
        OI -> robot_py
        constants_py -> robot_py
        constants_py -> subsystems
        constants_py -> sensors
        constants_py -> utils
        config_py -> subsystems
        config_py -> sensors
        subsystem -> robot_systems_py
        sensors -> robot_systems_py
        utils -> subsystems
        utils -> commands
        robot_systems_py -> robot_py
        subsystems -> tests
        commands -> tests
        sensors -> tests
    }