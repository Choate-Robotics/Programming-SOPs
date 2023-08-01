========================
Hardware and Electronics
========================

This page covers the hardware and electronics used on the robot that we utilize often.

Core Components
===============

Every Robot we work on will have all of these components. They are the most important parts of the robot and are used in every subsystem.

RoboRIO
-------

The RoboRIO is the main controller for the robot. It is a National Instruments controller that runs a real-time operating system. It is programmed in LabVIEW, C++, Java, or in our case, Python. The RoboRIO is connected to the PDP, radio, and motor controllers.

* This is where the code is run
* [RoboRIO Documentation](http://www.ni.com/pdf/manuals/374474a.pdf)
* [RoboRIO Pinout](http://www.ni.com/pdf/manuals/374474a.pdf#page=8)


PDH
---

The Power Distribution Hub (PDH) is a device that distributes power to the motor controllers and RoboRIO. It also monitors the current draw of each motor controller and the RoboRIO. The PDP is connected to the RoboRIO, motor controllers, and battery.

CAN Wires:
---------

The CAN Loop is a network of devices that communicate with each other. The RoboRIO, PDP, and motor controllers are all connected to the CAN Loop. The CAN Loop is used to send commands to the motor controllers and to monitor the current draw of each motor controller. Each device on the CAN loop has an ID which is used to recieve and send data.

* Almost 100% of our robot's electronics are connected to the CAN Loop (EX: RoboRIO, PDP, Motor Controllers, etc.), and is the main way we communicate with the electronics

Radio:
------

The radio is a device that allows the RoboRIO to communicate with the driver station. It is connected to the RoboRIO and the PDP. The radio is used to send data to the driver station and to recieve data from the driver station. The radio is also used to connect to the robot wirelessly.

* This device is used to communicate with the driver station

Networktables:
--------------

Networktables is a way for the RoboRIO to communicate with the driver station. It is used to send data to the driver station and to recieve data from the driver station. Networktables is used to send data such as the robot's position, the robot's speed, and the robot's angle. Networktables is also used to recieve data such as the joystick's position, the joystick's button presses, and the joystick's angle.

* We use Networktables to send data between other devices on the robot, the RoboRIO, and the driver station (EX: Limelight)

* [Networktables Documentation](http://robotpy.readthedocs.io/en/stable/guide/nt.html)