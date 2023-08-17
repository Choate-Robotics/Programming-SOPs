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




CAN Wires:
---------

.. figure:: https://www.mindsensors.com/406-thickbox_default/can-cable.jpg
    :align: center
    
    The CAN Wires are used to connect the RoboRIO, PDP, and motor controllers together. The CAN Wires are connected to the RoboRIO, PDP, and motor controllers.


.. The CAN Loop is a network of devices that communicate with each other. The RoboRIO, PDP, and motor controllers are all connected to the CAN Loop. The CAN Loop is used to send commands to the motor controllers and to monitor the current draw of each motor controller. Each device on the CAN loop has an ID which is used to recieve and send data.

* Almost 100% of our robot's electronics are connected to the CAN Loop (EX: RoboRIO, PDP, Motor Controllers, etc.), and is the main way we communicate with the electronics

Radio:
------

.. figure:: https://cdn.andymark.com/product_images/open-mesh-om5p-ac-dual-band-1-17-gbps-access-point-radio/am-3205/5c33d218fe93c61bdeff9b12/detail.jpg?c=1546899992
    :align: center
    
    The radio is a device that allows the RoboRIO to communicate with the driver station. It is connected to the RoboRIO and the PDP. The radio is used to send data to the driver station and to recieve data from the driver station. The radio is also used to connect to the robot wirelessly.

.. The radio is a device that allows the RoboRIO to communicate with the driver station. It is connected to the RoboRIO and the PDP. The radio is used to send data to the driver station and to recieve data from the driver station. The radio is also used to connect to the robot wirelessly.

* This device is used to communicate with the driver station


Motor Controllers
=================

Rev Spark Max
-------------

.. figure:: https://cdn11.bigcommerce.com/s-t3eo8vwp22/images/stencil/1280x1280/products/360/2795/MAX_HERO-noflag__60247.1650573462.png?c=2
    :align: center
    
    The Spark Max is a motor controller that controls the brushless motors. The Spark Max is connected to the RoboRIO, PDH, and brushless motors through the CAN Loop.

CTRE Falcon 500
---------------

.. figure:: https://cdn11.bigcommerce.com/s-7cuph2j78p/images/stencil/1280x1280/products/134/643/3__19352.1673993701.png?c=1
    :align: center
    
    The Falcon 500 is a motor with a built-in motor controller. The Falcon 500 is connected to the RoboRIO, PDH, and brushless motors through the CAN Loop.


Inputs
======

Digital Input
-------------

.. figure:: https://cdn11.bigcommerce.com/s-t3eo8vwp22/images/stencil/1280w/products/242/2787/Button_Sensor_REV-31-1425_1_not_lm__59552.1650572155.png?c=2
    :align: center
    
    The Digital Input is a device that detects if a digital signal is high or low (like a button). The Digital Input is connected to the RoboRIO DIO ports and the digital sensor.

    * You can think of it as a 0 or 1, or a True or False
    * These are used for limit switches, buttons, etc.



Analog Input
------------

.. figure:: https://cdn11.bigcommerce.com/s-t3eo8vwp22/images/stencil/1280x1280/products/340/2734/2M_Distance_Sensor__87798.1650562207.png?c=2
    :align: center
    
    The Analog Input is a device that detects the voltage of an analog signal (like a distance sensor). The Analog Input is connected to the RoboRIO PWM port and the analog sensor.

    * you can think of it as a range of values between 0 and 1, like 0.5 or 0.25
    * These are used for distance sensors, potentiometers, etc.


.. note::
    We usually connect digital and analog sensors that relate to motor movement to the motor controllers, not the RoboRIO. This is because the RoboRIO is slower than the motor controllers, so the motor controllers can react faster to the sensor.

    .. figure:: https://cdn11.bigcommerce.com/s-t3eo8vwp22/images/stencil/1280x1280/products/387/1270/Spark_Max_Data_Port_Breakout_Board_Lone__47117.1548200358.png?c=2
        :align: center

        this plugs into the data-port on the Spark Max


Vision Processors
=================

Limelight
---------

.. figure:: https://limelightvision.io/cdn/shop/products/L2SCALED_2048x.png?v=1674663124
    :align: center
    
    The Limelight is a vision processor that detects the location of the target. The Limelight is connected to the RoboRIO and the camera.

    * This is used for vision tracking with retroReflective tape, Feducials, and neural networks


