Swerve Drive
=============

Swerve drive is a type of drivetrain that allows a robot to move in any direction without turning. Each wheel operates independently, with the ability to rotate to a specific angle and drive at a specific speed, which allows the robot to move in any direction. This type of drivetrain is widely used in various robotics applications, including FIRST Robotics Competition (FRC) robots, due to its flexibility and enhanced maneuverability.

One of the main advantages is that it allows the robot to move in any direction without turning, which can be very useful in FRC games where the robot needs to cycle quickly across the field. Another advantage is that the robot can strafe or move sideways, which helps avoid defense bots or obstacles. Robots can also turn in place, which is useful for lining up shots or navigating tight spaces. It increases maneuverability and allows for more precise control of the robot. Swerve is also very effective if your robot needs to aim a shooter or other mechanism while moving. You can rotate in the robot while also moving toward the target.

.. figure:: https://i.ibb.co/2qLNCnP/9hhpas.gif
   :alt: PID Control
   :align: center

Swerve drives are made up of some number of, usually four, modules. These modules are made up of a wheel and a motor
that can rotate the wheel. The wheel is mounted on a turntable that can rotate the wheel to any angle. One motor is
used to drive the wheel at the desired speed. The angle of the wheel is controlled by another motor.

If all the wheels are at the same angle and speed then the robot will move in a straight line. If the wheels are at
at an angle perpendicular to the line that connects the wheel to the center of the robot and all the all the wheels are
powered equally then the robot will rotate in place. Thinking of these settings as vectors, you can use vector addition
to calculate the direction and speed necessary to make the robot do both of these things at the same time.

The main disadvantage of swerve drive is that it is more complex than other drive trains. This means that it can be more
difficult to design, build, and program. Swerve drive also requires more motors than other drive trains, which can be a
limiting factor in some games.

Programming a Swerve Drive:
---------------------------

Programming a Swerve is generally going to take several different abstractions. The first is the **SwerveModule**.
This will be a class that represents a single swerve module. It will have a method to set the speed and angle of the
wheel. It will also have a method to get the current speed and angle of the wheel.

The next abstraction is the **SwerveDrive**. This will be a class that represents the entire swerve drive. It will have
a method to set the speed and angle of the entire robot. It will also have a method to get the current speed and angle
of the entire robot. It will have a method to get the current speed and angle of each wheel. It will also have a method
to set the speed and angle of each wheel.

Another abstraction is the **SwerveDriveController**. This will be a class that represents the controller for the swerve
drive. It will have a method to get the desired speed and angle of the robot. It will also have a method to get the desired
speed and angle of each wheel. It will have a method to set the desired speed and angle of the robot. It will also have a
method to set the desired speed and angle of each wheel.

Another abstraction that is generally used is the **SwerveDriveKinematics**. This will be a class that represents the
kinematics of the swerve drive. It will have a method to calculate the speed and angle of each wheel given the speed and
angle of the robot. It will also have a method to calculate the speed and angle of the robot given the speed and angle of
each wheel.

Each swerve drive is generally made up of a series of **SwerveNodes**. These are the individual wheels that make up the
swerve drive. Generally what the swerve code needs to do is determine the speed and angle for each of the swerve nodes to
get the robot to move in the desired direction. This is generally done by calculating with the speed and angle of the robot

Finally there is the **ChassisSpeeds** class. This will be a class that represents the speed of the robot. It will have
a method to get the speed of the robot in the x direction. It will also have a method to get the speed of the robot in the
y direction. It will have a method to get the speed of the robot rotating.

Swerve Drive on 7407
--------------------

On 7407, the swerve drive code is often used based on the code that we used in previous years. This code has been written
with an eye to allow us to use encoder information, camera information, and gyro to get accurate odometry to allow use to
write autonomous code that can be used to navigate the field. Check out code in the ``toolkit`` folder of the template repo.

