==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:

.. graphviz::

    digraph file_structure {
        node [shape=box, style=filled, fontname=helvetica]

        // Clusters for folders
        subgraph cluster_commands {
            label="commands/"
            color=blue
            style=filled
            fillcolor=lightblue
            commands [label="__init__.py"]
            command1_py [label="command1.py"]
            command2_py [label="command2.py"]
            // Add more example files in the commands folder, if needed
        }

        subgraph cluster_subsystems {
            label="subsystem/"
            color=orange
            style=filled
            fillcolor=lightsalmon
            subsystems [label="__init__.py"]
            subsystem1_py [label="subsystem1.py"]
            subsystem2_py [label="subsystem2.py"]
            // Add more example files in the subsystem folder, if needed
        }

        subgraph cluster_oi {
            label="oi/"
            color=purple
            style=filled
            fillcolor=thistle
            oi_py [label="oi.py"]
            Keymap_py [label="Keymap.py"]
            // Add more example files in the oi folder, if needed
        }

        subgraph cluster_sensors {
            label="sensors/"
            color=green
            style=filled
            fillcolor=palegreen
            sensors [label="__init__.py"]
            sensor1_py [label="sensor1.py"]
            sensor2_py [label="sensor2.py"]
            // Add more example files in the sensors folder, if needed
        }

        subgraph cluster_utils {
            label="utils/"
            color=red
            style=filled
            fillcolor=lightcoral
            utils [label="__init__.py"]
            util1_py [label="util1.py"]
            util2_py [label="util2.py"]
            // Add more example files in the utils folder, if needed
        }

        subgraph cluster_tests {
            label="tests/"
            color=grey
            style=filled
            fillcolor=lightgrey
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
        constants_py -> subsystem1_py [color=orange, style=bold]
        config_py -> subsystem1_py [color=orange, style=bold]
        constants_py -> subsystem2_py [color=orange, style=bold]
        config_py -> subsystem2_py [color=orange, style=bold]

        // Sensor connections
        constants_py -> sensor1_py [color=green, style=bold]
        config_py -> sensor1_py [color=green, style=bold]
        constants_py -> sensor2_py [color=green, style=bold]
        config_py -> sensor2_py [color=green, style=bold]

        // Robot system connections
        subsystems -> robot_systems_py [color=black, style=dashed]
        sensors -> robot_systems_py [color=black, style=dashed]

        // Command connections
        subsystems -> commands [color=blue, style=bold]
        sensors -> commands [color=blue, style=bold]

        // OI connections
        commands -> oi_py [color=purple, style=bold]

        // Utils connections
        util1_py -> subsystem1_py [color=red, style=bold]
        util2_py -> subsystem1_py [color=red, style=bold]
        util1_py -> subsystem2_py [color=red, style=bold]
        util2_py -> subsystem2_py [color=red, style=bold]

        // Test connections
        commands -> test_commands [color=grey, style=dashed]
        subsystems -> test_subsystems [color=grey, style=dashed]
        oi_py -> test_oi [color=grey, style=dashed]
        sensors -> test_sensors [color=grey, style=dashed]
        utils -> test_utils [color=grey, style=dashed]

        // Robot connections
        constants_py -> robot_py [color=black, style=dotted]
        config_py -> robot_py [color=black, style=dotted]
        oi_py -> robot_py [color=black, style=dotted]
        robot_systems_py -> robot_py [color=black, style=dotted]
        commands -> robot_py [color=black, style=dotted]

        // Adjust alignment and spacing
        {rank=same; subsystem1_py; subsystem2_py}
        {rank=same; sensor1_py; sensor2_py}
        {rank=same; robot_py; constants_py; config_py; oi_py; robot_systems_py}
    }


...yeah, that's a lot of stuff. Let's break it down.



