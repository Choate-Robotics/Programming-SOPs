==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:

.. graphviz::


    digraph file_structure {

        subgraph subsystems {
            subsystem1_py [label="subsystem1.py"]
            subsystem2_py [label="subsystem2.py"]
        }

        subgraph commands {
            command1_py [label="command1.py"]
            command2_py [label="command2.py"]
        }

        subgraph oi {
            oi_py [label="oi.py"]
            Keymap_py [label="Keymap.py"]
            Keymap_py -> oi_py
        }

        subgraph tests {
            commands_tests_py [label="commands.py"]
            subsystems_tests_py [label="subsystems.py"]
            sensors_tests_py [label="sensors.py"]
            utils_tests_py [label="utils.py"]
        }

        subgraph utils {
            util1_py [label="util1.py"]
            util2_py [label="util2.py"]
        }

        subgraph sensors {
            sensor1_py [label="sensor1.py"]
            sensor2_py [label="sensor2.py"]
        }

        robot_py [label="robot.py"]
        robot_systems_py [label="robot_systems.py"]
        constants_py [label="constants.py"]
        config_py [label="config.py"]

        subsystems -> robot_subsystems_py
        sensors -> robot_systems_py
        robot_systems_py -> commands
        robot_systems_py -> robot_py
        subsystems -> commands
        commands -> robot_py
        constants_py -> robot_py
        config_py -> robot_py
        constants_py -> subsystems
        constants_py -> commands
        config_py -> subsystems
        
        
    }