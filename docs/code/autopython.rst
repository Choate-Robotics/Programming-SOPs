==================
Python Auto Example and Instructions
==================

Here is a code sample for how to make an auto in Python. Keep in mind, added files and variables such as the drivetrain 
will need to be imported from your codebase. Also, make sure to change the functions in our example code 
to similar ones in your codebase.

Here is a sample code from our four piece L4 right auto. It might be a lot to take in at once, so we'll split it 
up in smaller, more understandable sections.

.. code-block:: python
    :linenos:

    from pathplannerlib.path import PathPlannerPath
    from pathplannerlib.auto import AutoBuilder

    from robot_systems import Robot, Field
    from utils.field import get_red_pose
    from command import *
    import config

    from wpilib import DriverStation
    from commands2 import SequentialCommandGroup, InstantCommand, ParallelCommandGroup

    path_name = "Four L4 Right"
    paths = [PathPlannerPath.fromChoreoTrajectory(path_name, i) for i in range(11)]
    starting_pose = get_red_pose(paths[0].getStartingHolonomicPose()) if DriverStation.getAlliance() == DriverStation.Alliance.kRed else paths[0].getStartingHolonomicPose()

    auto = SequentialCommandGroup(
        InstantCommand(lambda: Robot.drivetrain.reset_odometry_auto(starting_pose)),
        InstantCommand(lambda: Robot.wrist.set_coral(True)),
        ParallelCommandGroup(
            Target(config.target_positions["IDLE"], Robot.wrist, Robot.elevator),
            AutoBuilder.followPath(paths[0]),
        ),
        ParallelCommandGroup(
            Target(config.target_positions["L3"], Robot.wrist, Robot.elevator),
            AutoBuilder.followPath(paths[1]),
        ),
        FeedOut(Robot.wrist).withTimeout(.2),
        ParallelCommandGroup( 
            Target(config.target_positions["STATION_INTAKING"], Robot.wrist, Robot.elevator),
            AutoBuilder.followPath(paths[2]),
        ),
        IntakeCoral(Robot.intake, Robot.wrist),
        AutoBuilder.followPath(paths[3]),
        ParallelCommandGroup(
            Target(config.target_positions["L3"]),
            AutoBuilder.followPath(paths[4]),
        ),
        FeedOut(Robot.wrist).withTimeout(.2),
        ParallelCommandGroup(
            AutoBuilder.followPath(paths[5]), 
            Target(config.target_positions["STATION_INTAKING"], Robot.wrist, Robot.elevator),
        ),
        IntakeCoral(Robot.intake, Robot.wrist),
        AutoBuilder.followPath(paths[6]),
        ParallelCommandGroup(
            AutoBuilder.followPath(paths[7]),
            Target(config.target_positions["L3"]),
        ),
        FeedOut(Robot.wrist).withTimeout(.2),
        ParallelCommandGroup(
            AutoBuilder.followPath(paths[8]),
            Target(config.target_positions["STATION_INTAKING"], Robot.wrist, Robot.elevator),
        ),
        IntakeCoral(Robot.intake, Robot.wrist),
        AutoBuilder.followPath(paths[9]),
        ParallelCommandGroup(
            AutoBuilder.followPath(paths[10]),
            Target(config.target_positions["L3"]),
        ),
        FeedOut(Robot.wrist).withTimeout(.2),
    )
*This sample was influenced by Team 7407's 2025 codebase.*

Imports 
=========
.. code-block:: python
    :linenos:

    from pathplannerlib.path import PathPlannerPath
    from pathplannerlib.auto import AutoBuilder

    from robot_systems import Robot, Field
    from utils.field import get_red_pose
    from command import *
    import config

    from wpilib import DriverStation
    from commands2 import SequentialCommandGroup, InstantCommand, ParallelCommandGroup

Here are our imports! We use PathPlanner to generate/map out and tune our paths, and import it
so we can assign robot functionalities to each of the different paths we follow on the field. 
(See our Path Planning documentation for more on this.) 

Then, we import the dimensions of the robot, game field, and poses we will incorporate to put 
our robot in certain positions on the field. 

Of course, we also want to import Driverstation as well as our Commands so we can actually do stuff.

.. note::
    We are importing *our* commands in line 6, which imports the commands we wrote using the methods from our 
    subsystems. In line 10, we import the *types* of commands we want to organize our robot commands into.
    This may sound a little confusing at first, but we'll get into the different types on a case by case basis.

Paths
=======

.. code-block:: python
    :linenos:

    path_name = "Four L4 Right"
    paths = [PathPlannerPath.fromChoreoTrajectory(path_name, i) for i in range(11)]
    starting_pose = get_red_pose(paths[0].getStartingHolonomicPose()) if DriverStation.getAlliance() == DriverStation.Alliance.kRed else paths[0].getStartingHolonomicPose()

In Choreo, the name of our auto trajectory was "Four L4 Right", so we will use this name as a parameter when creating a list of our paths.
The number of elements in this list is the number of paths in our Choreo trajectory, which in this case is 11.
We also define our starting pose (You can think of this as a starting position.) as what we have in Driver Station based on what alliance we're on.

The Actual Auto
=================

.. code-block:: python
    :linenos:

    auto = SequentialCommandGroup(...)

This is where we actually create our auto. 
Since we want our commands to run in order, we set it equal to a sequential command group. All this does is run the 
commands in the order they are typed, starting the next command only when the previous one has finished. 

.. note:: 
    Remember to separate each command with a comma! You'll see this later on...

Instant Commands
==================

.. code-block:: python
    :linenos:

    auto = SequentialCommandGroup(
        InstantCommand(lambda: Robot.drivetrain.reset_odometry_auto(starting_pose)),
        InstantCommand(lambda: Robot.wrist.set_coral(True)),
        ...)

Autos can consist of any commands, and they will vary based on the auto you are writing. In this auto, we start with 
two instant commands: one that resets the odometry of the drivetrain to the starting pose, and one that sets the 
boolean for coral in the wrist as true*. Instant commands do whatever is inside the parenthesis *instantaneously*.

* We already have a coral preloaded in our reset before the match.

The Rest of the Auto
======================

.. code-block:: python
    :linenos:

    auto = SequentialCommandGroup(
        InstantCommand(lambda: Robot.drivetrain.reset_odometry_auto(starting_pose)),
        InstantCommand(lambda: Robot.wrist.set_coral(True)),
        ParallelCommandGroup(
            Target(config.target_positions["IDLE"], Robot.wrist, Robot.elevator),
            AutoBuilder.followPath(paths[0]),
        ),
        ParallelCommandGroup(
            Target(config.target_positions["L3"], Robot.wrist, Robot.elevator),
            AutoBuilder.followPath(paths[1]),
        ),
        FeedOut(Robot.wrist).withTimeout(.2),
        ParallelCommandGroup( 
            Target(config.target_positions["STATION_INTAKING"], Robot.wrist, Robot.elevator),
            AutoBuilder.followPath(paths[2]),
        ),
        IntakeCoral(Robot.intake, Robot.wrist),
        AutoBuilder.followPath(paths[3]),
        ParallelCommandGroup(
            Target(config.target_positions["L3"]),
            AutoBuilder.followPath(paths[4]),
        ),
        FeedOut(Robot.wrist).withTimeout(.2),
        ParallelCommandGroup(
            AutoBuilder.followPath(paths[5]), 
            Target(config.target_positions["STATION_INTAKING"], Robot.wrist, Robot.elevator),
        ),
        IntakeCoral(Robot.intake, Robot.wrist),
        AutoBuilder.followPath(paths[6]),
        ParallelCommandGroup(
            AutoBuilder.followPath(paths[7]),
            Target(config.target_positions["L3"]),
        ),
        FeedOut(Robot.wrist).withTimeout(.2),
        ParallelCommandGroup(
            AutoBuilder.followPath(paths[8]),
            Target(config.target_positions["STATION_INTAKING"], Robot.wrist, Robot.elevator),
        ),
        IntakeCoral(Robot.intake, Robot.wrist),
        AutoBuilder.followPath(paths[9]),
        ParallelCommandGroup(
            AutoBuilder.followPath(paths[10]),
            Target(config.target_positions["L3"]),
        ),
        FeedOut(Robot.wrist).withTimeout(.2),
    )

This part gets a little repetitive, but here's the gist: 
- AutoBuilder.followPath(paths[i]) follows path i in our choreo trajectory
- We utilize the fact that the entire auto is in a Sequential Command Group, to run all of the tasks in order: 
following a path and then doing tasks at the location it ends up at
- You might notice we also use Parallel Command Groups, which run multiple commands in parallel. We use them to follow 
the paths in our Choreo trajectory while also moving the robot subsystems.

Congratulations! You have just learned how to code an auto. 