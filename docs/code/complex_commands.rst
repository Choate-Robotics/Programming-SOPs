=========================
Complex Commands Overview
=========================

The `controller.py` module in our repository provides a framework for managing complex commands in robotic control systems. It offers structured classes to handle various command types, ensuring efficient execution and management. It merges all commands together to create a "master command" where all subsystems can be called.

Key Components
==============

Command Base Class
------------------
The base class for all commands, defining essential methods:

- `initialize`: Preparation steps before execution. Add new variables, methods, etc.
- `execute`: The main logic of the command. Runs the method in subsystem you call, catches any errors.
- `end`: Cleanup after execution. Makes sure all subsystems are in a safe state.
- `isFinished`: Determines if the command has completed. If interrupted, you can handle an error. Takes in `interrupted` as a parameter "bool"

This structure ensures a consistent interface for all commands. 

Types of Commands
=================

SequentialCommandGroup
----------------------
Executes a list of commands in sequence, starting the next command only after the current one finishes. Useful for tasks requiring a specific order of operations.

ParallelCommandGroup
--------------------
Runs multiple commands simultaneously, allowing for concurrent operations. Beneficial when multiple subsystems need to operate at the same time.

ConditionalCommand
------------------
Chooses between two commands based on a runtime-evaluated condition, enabling dynamic decision-making within the command structure.