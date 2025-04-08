===============
Creating Subsystems 
===============

Welcome to our tutorial for creating subsystems! 
Before jumping in, it's recommended that you're vaguely familiar with OOP concepts, 
but as long as you know what a class, method, and property is, you'll be fine!

The following code is a sample from 7407's 2025 code base. 

.. code-block:: python
    :linenos:
    import ntcore
    from wpilib import DigitalInput

    import config
    import constants
    from toolkit.motors.ctre_motors import TalonFX
    from toolkit.subsystem import Subsystem
    from units.SI import meters, meters_to_inches

    class Elevator(Subsystem):
        def __init__(self):
            super().__init__()
            self.leader_motor: TalonFX = TalonFX(
                config.elevator_lead_id,
                config.foc_active,
                inverted=False,
                config=config.ELEVATOR_CONFIG
            )
            self.follower_motor: TalonFX = TalonFX(
                config.elevator_follower_id,
                config.foc_active,
                inverted=False,
                config=config.ELEVATOR_CONFIG
            )

            self.target_height: meters = 0.0
            self.elevator_moving: bool = False

        def init(self):
            self.leader_motor.init()
            self.follower_motor.init()
            self.follower_motor.follow(self.leader_motor, inverted=True)
            self.leader_motor.set_sensor_position(0)

        @staticmethod
        def limit_height(height: meters) -> meters:
            """
            limits the height of the elevator to both a max and min
            """
            if height > constants.elevator_max_height:
                return constants.elevator_max_height
            elif height < 0.0:
                return 0.0
            return height

        def set_position(self, height: meters) -> None:
            """
            Brings the elevator to given height

            Args:
                height (meters): intended elevator height in meters
            """
            height = self.limit_height(height)
            self.target_height = height

            rotations = (
                height * constants.elevator_gear_ratio
            ) / constants.elevator_driver_gear_circumference
            self.leader_motor.set_target_position(rotations)

        def stop(self) -> None:
            """
            Stops the elevator
            """
            self.set_position(self.get_position())

        def set_zero(self) -> None:
            """
            Brings the elevator to the zero position
            """
            self.set_position(0)

        def get_position(self) -> meters:
            """
            Obtains the current height of the elevator

            Returns:
                return_float: current elevator height in meters
            """
            return (
                self.leader_motor.get_sensor_position()
                * constants.elevator_driver_gear_circumference
                / constants.elevator_gear_ratio
            )

        def is_at_position(self, height: meters) -> bool:
            """
            checks if the elevator is at a certain height

            Args:
                height (meters): height to be checked
            """
            return abs(self.get_position() - height) < config.elevator_height_threshold

        def update_table(self) -> None:
            table = ntcore.NetworkTableInstance.getDefault().getTable("Elevator")

            table.putNumber("height", self.get_position() * meters_to_inches)
            table.putNumber("velocity rps", self.leader_motor.get_sensor_velocity())
            table.putNumber("acceleration rpss", self.leader_motor.get_sensor_acceleration())
            table.putNumber("target height", self.target_height * meters_to_inches)
            table.putNumber(
                "motor lead applied output", self.leader_motor.get_applied_output()
            )
            table.putNumber(
                "motor lead current", self.leader_motor.get_motor_current()
            )
            table.putNumber(
                "motor follow applied output", self.follower_motor.get_applied_output()
            )

        def periodic(self):
            if config.NT_ELEVATOR:
                self.update_table()


Imports 
=======

.. code-block:: python
    :linenos:
    import ntcore
    from wpilib import DigitalInput

    import config
    import constants
    from toolkit.motors.ctre_motors import TalonFX
    from toolkit.subsystem import Subsystem
    from units.SI import meters, meters_to_inches

Of course, we need to import config, constants, our motor's class (so we can use methods from it), and any units we need for conversions.
In line 7, we import the Subsystem class in toolkit that we inherit from, and generally use as a template when
creating a new subsystem class. 

Creating the subsystem
========

.. code-block:: python
    :linenos:
     class Elevator(Subsystem):

        def __init__(self):
            super().__init__()
            ...
        def init(self):
            ...

We create a new class--Elevator, in this case--that inherits from our Subsystem class that we imported 
from toolkit. For now, we're putting an ellipsis where most of the actual stuff happens so that
we can explain subsystem structure.

In our dunder* init method (line 3), we put any properties we will use in our later methods, 
and create our motors. Also, since we are inheriting from a class, we have a super in there. (line 4)

In our regular init method (line 6), we run methods that initialize our motors, and also any other 
methods that we want to run when initializating our elevator. (like setting our starting position to 0)

Another key difference between these two methods is that the dunder init method is automatically
called when a new instance of the class is created, and the init method is called by us when we 
want to run methods to set everything up before running any other methods.

* dunder means double underscore

MOTORS
========

.. code-block:: python
    :linenos:
    class Elevator(Subsystem):

            def __init__(self):
                super().__init__()
                self.leader_motor: TalonFX = TalonFX(
                    config.elevator_lead_id,
                    config.foc_active,
                    inverted=False,
                    config=config.ELEVATOR_CONFIG
                )
                self.follower_motor: TalonFX = TalonFX(
                    config.elevator_follower_id,
                    config.foc_active,
                    inverted=False,
                    config=config.ELEVATOR_CONFIG
                )

                self.target_height: meters = 0.0 #see note no. 2
                self.elevator_moving: bool = False # ^^

            def init(self):
                self.leader_motor.init()
                self.follower_motor.init()
                self.follower_motor.follow(self.leader_motor, inverted=True)
                self.leader_motor.set_sensor_position(0)

Get excited, because now we're going to explain everything you might ever want to know about **motors**!

In general, this is how you would create, for example, a TalonFX motor: (Remember, this is done in __init__())

.. code-block:: python
    :linenos:
    self.motor_name: TalonFX = TalonFX(
        config.motor_id, #this property's value is stored in config
        config.foc_active, 
        inverted=False, #not in the reverse direction
        config=config.ELEVATOR_CONFIG #every other parameter value for the motor 
        )

Later, in init(), we initialize the motors. This is when we establish our leader and follower motors. (When we created
them we named them accordingly, for simplicity.) Using a method from the motor libraries, in line 24 we assign the follower_motor
to follow the leader_motor. Here is the syntax for the method that does this:
def follow(self, master: TalonFX, inverted: bool = False)

.. note:: 
    When we create our motors for this subsystem, we chose to use a leader and a follower motor. In case 
    you weren't already aware:
    The relationship between a leader and follower motor is exactly as it sounds! Instead of having to apply 
    methods to each motor individually, you just apply the methods to the leader motor, and the follower motor 
    will do the same things.

.. note::
    As seen previously in lines 18-19 of our first code block in the section...

    .. code-block:: python
        :linenos:
            self.target_height: meters = 0.0 
            self.elevator_moving: bool = False

    target_height and elevator_moving are both properties whose values we want to keep track of later
    on in our code. 