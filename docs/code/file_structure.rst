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
            commands [label=""]
            command1_py [label="command1.py"]
            command2_py [label="command2.py"]
            // Add more example files in the commands folder, if needed
        }

        subgraph cluster_subsystem {
            label="subsystem/"
            subsystem [label=""]
            subsystem1_py [label="subsystem1.py"]
            subsystem2_py [label="subsystem2.py"]
            // Add more example files in the subsystem folder, if needed
        }

        subgraph oi {
            oi_py [label="oi.py"]
            Keymap_py [label="Keymap.py"]
            Keymap_py -> oi_py
        }



        robot_py [label="robot.py"]
        robot_systems_py [label="robot_systems.py"]
        constants_py [label="constants.py"]
        config_py [label="config.py"]

        subsystems -> robot_systems_py
        commands -> robot_py

        
    }