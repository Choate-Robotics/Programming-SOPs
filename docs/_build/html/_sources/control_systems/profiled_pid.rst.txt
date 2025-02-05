
Profiled PID Control
=====================

Profiled PID control, similar to regular PID control, is a control loop feedback mechanism that incorporates acceleraton and velocity limits with a trapezoidal constraint.


.. note::
    for a review on PID control, see `PID <pid.rst>`_

A profiled PID is used over normal PID when the system being controlled has physical constraints on acceleration and velocity. For example, a robot arm may have a maximum acceleration and velocity that it can achieve. A profiled PID will take these constraints into account when generating the control signal.

The profiled PID is implemented as a subclass of the regular PID class. The profiled PID class overrides the :meth:`PIDController.calculate` method to add the acceleration and velocity constraints.

The profiled PID class also adds two new methods, :meth:`PIDController.setAccelerationLimits` and :meth:`PIDController.setVelocityLimits`, which set the acceleration and velocity limits, respectively.

You can create a profiled PID controller using the :class:`ProfiledPIDController` class.

.. code-block:: python

    from wpilib.controller import ProfiledPIDController
    from wpilib.trajectory import TrapezoidProfile

    constraints = TrapezoidProfile.Constraints(max_velocity=1.7, max_acceleration=2)

    controller = ProfiledPIDController(1, 0, 0, constraints=constraints)

    # Set the goal state

    controller.setGoal(TrapezoidProfile.State(3, 0))

    # Calculate the feedforward and feedback terms

    output = controller.calculate(current_pose, current_velocity)

    # Use the output to control the mechanism

    mechanism.setVoltage(output)


.. note::

    The :class:`ProfiledPIDController` class is a subclass of the :class:`PIDController` class. This means that you can use a profiled PID controller anywhere you would use a regular PID controller. For example, you can use a profiled PID controller in the :class:`wpilib.controller.RamseteController` class.

    .. code-block:: python

        from wpilib.controller import RamseteController
        from wpilib.trajectory import Trajectory

        trajectory = Trajectory()

        controller = RamseteController(2, 0.7)

        # Set the goal state

        controller.setGoal(trajectory.sample(0))

        # Calculate the feedforward and feedback terms

        output = controller.calculate(current_pose, current_velocity)

        # Use the output to control the mechanism

        mechanism.setVoltage(output)
