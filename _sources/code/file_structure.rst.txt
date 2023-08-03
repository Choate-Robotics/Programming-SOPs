==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:

.. graphviz::

    digraph file_structure {

        node [shape=box, style=filled, color=lightgrey, fontname=helvetica]

        // Clusters for folders
        subgraph cluster_commands {
            label="commands/"
            commands [label="__init__.py"]
            command1_py [label="command1.py"]
            command2_py [label="command2.py"]
            // Add more example files in the commands folder, if needed
        }

        subgraph cluster_subsystems {
            label="subsystem/"
            subsystems [label="__init__.py"]
            subsystem1_py [label="subsystem1.py"]
            subsystem2_py [label="subsystem2.py"]
            // Add more example files in the subsystem folder, if needed
        }

        subgraph cluster_oi {
            label="oi/"
            oi_py [label="oi.py"]
            Keymap_py [label="Keymap.py"]
            // Add more example files in the oi folder, if needed
        }

        subgraph cluster_sensors {
            label="sensors/"
            sensors [label="__init__.py"]
            sensor1_py [label="sensor1.py"]
            sensor2_py [label="sensor2.py"]
            // Add more example files in the sensors folder, if needed
        }

        subgraph cluster_utils {
            label="utils/"
            utils [label="__init__.py"]
            util1_py [label="util1.py"]
            util2_py [label="util2.py"]
            // Add more example files in the utils folder, if needed
        }

        subgraph cluster_tests {
            label="tests/"
            test_commands [label="commands/"]
            test_subsystems [label="subsystems/"]
            test_oi [label="oi/"]
            test_sensors [label="sensors/"]
            test_utils [label="utils/"]
        }

        // Files in the root
        robot_py [label="robot.py"]
        robot_systems_py [label="robot_systems.py"]
        constants_py [label="constants.py"]
        config_py [label="config.py"]

        // Subsystem connections
        constants_py -> subsystem1_py
        config_py -> subsystem1_py
        constants_py -> subsystem2_py
        config_py -> subsystem2_py

        // Sensor connections
        constants_py -> sensor1_py
        config_py -> sensor1_py
        constants_py -> sensor2_py
        config_py -> sensor2_py

        // Robot system connections
        subsystems -> robot_systems_py
        sensors -> robot_systems_py

        // Command connections
        subsystems -> command1_py
        sensors -> command1_py
        subsystems -> command2_py
        sensors -> command2_py

        // OI connections
        commands -> oi_py

        // Utils connections
        util1_py -> subsystem1_py
        util2_py -> subsystem1_py
        util1_py -> subsystem2_py
        util2_py -> subsystem2_py

        // Test connections
        commands -> test_commands
        subsystems -> test_subsystems
        oi_py -> test_oi
        sensors -> test_sensors
        utils -> test_utils

        // Robot connections
        constants_py -> robot_py
        config_py -> robot_py
        oi_py -> robot_py
        robot_systems_py -> robot_py
        commands -> robot_py

        // Adjust alignment and spacing
        {rank=same; subsystem1_py; subsystem2_py}
        {rank=same; sensor1_py; sensor2_py}
        {rank=same; robot_py; constants_py; config_py; oi_py; robot_systems_py}
    }


...yeah, that's a lot of stuff. Let's break it down.



