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
            command1_py -> commands
            command2_py -> commands
            // Add more example files in the commands folder, if needed
        }

        subgraph cluster_subsystems {
            label="subsystem/"
            subsystems [label="__init__.py"]
            subsystem1_py [label="subsystem1.py"]
            subsystem2_py [label="subsystem2.py"]
            subsystem1_py -> subsystems
            subsystem2_py -> subsystems
            // Add more example files in the subsystem folder, if needed
        }

        subgraph cluster_oi {
            label="oi/"
            oi_py [label="oi.py"]
            Keymap_py [label="Keymap.py"]
            Keymap_py -> oi_py
        }

        subgraph cluster_sensors {
            label="sensors/"
            sensors [label="__init__.py"]
            sensor1_py [label="sensor1.py"]
            sensor2_py [label="sensor2.py"]
            sensor1_py -> sensors
            sensor2_py -> sensors
            // Add more example files in the sensors folder, if needed
        }



        robot_py [label="robot.py"]
        robot_systems_py [label="robot_systems.py"]
        constants_py [label="constants.py"]
        config_py [label="config.py"]

        // subsystem connections
        constants_py -> subsystem1_py
        config_py -> subsystem1_py
        subsystems -> subsystem1_py
        config_py -> subsystem2_py

        // robot system connections
        subsystems -> robot_systems_py
        sensors -> robot_systems_py

        // command connections
        subsystems -> command1_py
        sensors -> command1_py
        subsystems -> command2_py
        sensors -> command2_py

        // oi connections
        commands -> oi_py

        // robot connections
        constants_py -> robot_py
        config_py -> robot_py
        oi_py -> robot_py
        robot_systems_py -> robot_py
        commands -> robot_py

        
    }