========================
Hardware and Electronics
========================

This page covers the hardware and electronics used on the robot that we utilize often.

System Diagram
==============

.. figure:: https://docs.wpilib.org/en/stable/_images/frc-control-system-layout-rev.svg
    :align: center
    
    This is a diagram of the FRC Control System. It shows how all of the components are connected to each other.


Core Components
===============

Every Robot we work on will have all of these components. They are the most important parts of the robot and are used in every subsystem.

RoboRIO
-------

.. figure:: https://cdn.andymark.com/product_images/ni-roborio-2/61535a8be281bc516843b3c1/detail.jpg?c=1632852619
   :align: center

   The RoboRIO is the main controller for the robot. It is a National Instruments controller that runs a real-time operating system. It is programmed in LabVIEW, C++, Java, or in our case, Python. The RoboRIO is connected to the PDP, radio, and motor controllers.

.. The RoboRIO is the main controller for the robot. It is a National Instruments controller that runs a real-time operating system. It is programmed in LabVIEW, C++, Java, or in our case, Python. The RoboRIO is connected to the PDP, radio, and motor controllers.

* This is where the code is run
* [RoboRIO Documentation](http://www.ni.com/pdf/manuals/374474a.pdf)
* [RoboRIO Pinout](http://www.ni.com/pdf/manuals/374474a.pdf#page=8)


PDH
---

.. figure:: https://cdn11.bigcommerce.com/s-t3eo8vwp22/images/stencil/1280x1280/products/602/2509/REV-11-1850-PDH-Hero-FINAL__41676.1641407456.png?c=2
    :align: center
    
    The Power Distribution Hub (PDH) is a device that distributes power to the motor controllers and RoboRIO. It also monitors the current draw of each motor controller and the RoboRIO. The PDP is connected to the RoboRIO, motor controllers, and battery.

.. The Power Distribution Hub (PDH) is a device that distributes power to the motor controllers and RoboRIO. It also monitors the current draw of each motor controller and the RoboRIO. The PDP is connected to the RoboRIO, motor controllers, and battery.


Pneumatic Hub
-------------

.. figure:: https://cdn11.bigcommerce.com/s-t3eo8vwp22/images/stencil/1280x1280/products/600/2510/REV-11-1852-PH-Hero-FINAL__53879.1641407488.png?c=2
    :align: center
    
    The Pneumatic Hub is a device that controls the solenoid valves, which control the pistons. The Pneumatic Hub is connected to the RoboRIO, solenoid valves, and battery.


Motor Controllers
-----------------

Rev Spark Max
~~~~~~~~~~~~~

.. figure:: https://cdn11.bigcommerce.com/s-t3eo8vwp22/images/stencil/1280x1280/products/360/2795/MAX_HERO-noflag__60247.1650573462.png?c=2
    :align: center
    
    The Spark Max is a motor controller that controls the brushless motors. The Spark Max is connected to the RoboRIO, PDH, and brushless motors through the CAN Loop.

CTRE Falcon 500
~~~~~~~~~~~~~~~

.. figure:: https://cdn11.bigcommerce.com/s-7cuph2j78p/images/stencil/1280x1280/products/134/643/3__19352.1673993701.png?c=1
    :align: center
    
    The Falcon 500 is a motor with a built-in motor controller. The Falcon 500 is connected to the RoboRIO, PDH, and brushless motors through the CAN Loop.

CAN Wires:
---------



The CAN Loop is a network of devices that communicate with each other. The RoboRIO, PDP, and motor controllers are all connected to the CAN Loop. The CAN Loop is used to send commands to the motor controllers and to monitor the current draw of each motor controller. Each device on the CAN loop has an ID which is used to recieve and send data.

* Almost 100% of our robot's electronics are connected to the CAN Loop (EX: RoboRIO, PDP, Motor Controllers, etc.), and is the main way we communicate with the electronics

Radio:
------

.. figure:: https://cdn.andymark.com/product_images/open-mesh-om5p-ac-dual-band-1-17-gbps-access-point-radio/am-3205/5c33d218fe93c61bdeff9b12/detail.jpg?c=1546899992
    :align: center
    
    The radio is a device that allows the RoboRIO to communicate with the driver station. It is connected to the RoboRIO and the PDP. The radio is used to send data to the driver station and to recieve data from the driver station. The radio is also used to connect to the robot wirelessly.

.. The radio is a device that allows the RoboRIO to communicate with the driver station. It is connected to the RoboRIO and the PDP. The radio is used to send data to the driver station and to recieve data from the driver station. The radio is also used to connect to the robot wirelessly.

* This device is used to communicate with the driver station

