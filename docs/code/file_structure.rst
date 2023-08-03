==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:

.. graphviz::

    digraph G {
        rankdir=LR;
        node [shape=record];
        subgraph cluster_0 {
            label="src";
            style=filled;
            color=lightgrey;
            node [style=filled,color=white];
            "main.cpp";
            "robot.cpp";
            "robot.h";
            "robotmap.h";
            "subsystems";
            "commands";
            "OI.h";
        }
        subgraph cluster_1 {
            label="subsystems";
            style=filled;
            color=lightgrey;
            node [style=filled,color=white];
            "subsystem1.cpp";
            "subsystem1.h";
            "subsystem2.cpp";
            "subsystem2.h";
        }
        subgraph cluster_2 {
            label="commands";
            style=filled;
            color=lightgrey;
            node [style=filled,color=white];
            "command1.cpp";
            "command1.h";
            "command2.cpp";
            "command2.h";
        }
        subgraph cluster_3 {
            label="OI";
            style=filled;
            color=lightgrey;
            node [style=filled,color=white];
            "OI.cpp";
            "OI.h";
        }
        "robot.cpp" -> "subsystems";
        "robot.cpp" -> "commands";
        "robot.cpp" -> "OI.h";
        "subsystems" -> "subsystem1.cpp";
        "subsystems" -> "subsystem2.cpp";
        "commands" -> "command1.cpp";
        "commands" -> "command2.cpp";
        "OI.h" -> "OI.cpp";
    }