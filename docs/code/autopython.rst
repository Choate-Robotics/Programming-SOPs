==================
Python Auto Example and Instructions
==================

Here is a code sample for how to make an auto in Python. Keep in mind, added files and variables such as the drivetrain 
will need to be imported from your codebase. Also, make sure to change the functions in our example code 
to similar ones in your codebase.

This sample was influenced by Team 7407's 2023 codebase.

.. code-block:: python
    :linenos:

    from dataclasses import dataclass

    import commands2
    from commands2 import (
        CommandBase,
        InstantCommand
    )
    from wpimath.geometry import Pose2d
    from robot_systems import Robot
    from utils import POIPose

    from robot_systems import Robot
    from utils import POIPose
    from math import radians
    
    @dataclass
    class AutoRoutine:

        initial_robot_pose: Pose2d
        command: CommandBase

        def run(self):
            init_robot_pose = self.initial_robot_pose
            Robot.drivetrain.gyro.reset_angle(POIPose(self.initial_robot_pose).get().rotation().radians())
            Robot.drivetrain.reset_odometry_auto(POIPose(self.initial_robot_pose).get())
            commands2.CommandScheduler.getInstance().schedule(self.command)

        def start_auto(self):
            Robot.drivetrain.set_raw_output(1).withTimeout(2.0).andThen(
                InstantCommand(lambda: Robot.drivetrain.set_raw_output(0), Robot.drivetrain)
            )

