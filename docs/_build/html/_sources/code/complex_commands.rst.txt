=========================
Complex Commands Overview
=========================

The `controller.py` module in the `7407-DriveCode-Reefscape` repository provides a framework for managing complex commands in robotic control systems. It offers structured classes to handle various command types, ensuring efficient execution and management.

Key Components
==============

Command Base Class
------------------
The base class for all commands, defining essential methods:

- `initialize`: Preparation steps before execution.
- `execute`: The main logic of the command.
- `end`: Cleanup after execution.
- `isFinished`: Determines if the command has completed.

This structure ensures a consistent interface for all commands.

SequentialCommandGroup
----------------------
Executes a list of commands in sequence, starting the next command only after the current one finishes. Useful for tasks requiring a specific order of operations.

ParallelCommandGroup
--------------------
Runs multiple commands simultaneously, allowing for concurrent operations. Beneficial when multiple subsystems need to operate at the same time.

ConditionalCommand
------------------
Chooses between two commands based on a runtime-evaluated condition, enabling dynamic decision-making within the command structure.

Usage Example (From `7407-DriveCode-Crescendo`)
=============

To create a complex command sequence that first raises an arm and then drives forward while spinning a mechanism:

.. code-block:: python

   raise_arm = RaiseArmCommand()
   drive_forward = DriveForwardCommand()
   spin_mechanism = SpinMechanismCommand()

   complex_command = SequentialCommandGroup([
       raise_arm,
       ParallelCommandGroup([drive_forward, spin_mechanism])
   ])

This structure ensures that the arm is raised before the robot drives forward and spins the mechanism concurrently.

By utilizing the constructs provided in `controller.py`, developers can build intricate command sequences that manage robot behaviors effectively, promoting modularity and reusability in code design.