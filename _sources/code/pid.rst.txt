PID Control
===========

.. figure:: https://www.google.com/url?sa=i&url=https%3A%2F%2Fplcynergy.com%2Fpid-controller%2F&psig=AOvVaw2hQid8IxX788rqph1034vG&ust=1699983383652000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCIjg1-DBwYIDFQAAAAAdAAAAABAH
   :alt: PID Control
   :align: center

PID (Proportional-Integral-Derivative) control is a widely used feedback control algorithm in engineering. It plays a crucial role in maintaining desired setpoints or target values in various systems, including robotics.

Proportional (P):
-----------------

The proportional term in a PID controller produces an output value that is proportional to the current error. It results in a control response that reduces the error by a certain factor. Increasing the proportional gain can make the system respond more aggressively but may lead to overshooting the setpoint.

Integral (I):
--------------

The integral term accounts for past errors by summing up the error values over time and applying a correction based on the accumulated error. It eliminates any residual steady-state error and helps the system reach the setpoint accurately.

Derivative (D):
----------------

The derivative term anticipates future error by calculating the rate of change of the error over time. It provides a control response to counteract rapid changes in error, preventing overshoot and oscillations.

Use of PID in First Robotics
=============================

First Robotics competitions often rely on PID controllers for precise control of various robot functions. Here's how PID control is utilized:

- Motor Control: PID loops can control motor speed or position to achieve consistent robot movements or maintain specific arm or shooter positions.

- Shooter Systems: PID controllers are used to precisely control shooter velocity and angle for accurate object launching.

- Autonomous Navigation: PID control helps the robot navigate to specific positions or follow predefined paths accurately, especially in autonomous modes.

- Stability and Balance: In situations where robots need to balance on platforms or manipulate objects delicately, PID control ensures stability and precise control.

Feedforward Control
====================

Feedforward control is a technique often used in conjunction with PID control. It helps anticipate and compensate for known disturbances or external forces, allowing the system to respond faster and reducing the reliance on PID corrections. In robotics, feedforward control is frequently used to account for factors like gravity, friction, or other known influences that affect the system's behavior.

For example, when a robot arm is lifting an object, feedforward control can consider the weight of the object and apply a control input to counteract the gravitational force. This reduces the error that the PID controller needs to correct, making the system more responsive and stable.
