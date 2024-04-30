==============
Driver Station
==============

The driver station are designated computers that the team will use regularly to control the robot.

Setup
-----

If you need to set up a new driver station, you will need to install the following software:

* FRC Game Tools - for the driver station software
* FRC WPILIB Suite (TOOLS ONLY) - for Shuffleboard and other utilities
* Radio Configuration Utility - for configuring the radio
* AdvantageScope - for recieving and recording data
* Pheonix Tuner - for configuring CTRE motor controllers and sensors
* Rev Hardware Client - for configuring Rev Robotics motor controllers

.. caution:: 
    DO NOT BE FOOLED!
    while the amount of software you need to install is small, the installation process is long and the software is large. 
    Please allow yourself at least 30 minutes to install the software.
    **DO NOT BELIEVE THAT YOU CAN INSTALL THE SOFTWARE IN 5 MINUTES!**
    
    * Also, make sure to test the software before competing. 
      You don't want to be caught with a non-functional driver station at a competition.
      The Event Organizers will give you a replacement as long as you ask.


Downloading and Installing the Software
---------------------------------------

1. First, download the First FRC Game Tools from the FIRST website.
   You can find the download link `here <https://www.ni.com/en/support/downloads/drivers/download.frc-game-tools.html#479842>`_.
   
   .. important:: 
    * Make sure to download the latest version of the software.
    * This will take a while to install, so you can do the next steps while it is installing.

  The important programs to pin are:

     * Driver Station
    
     * RoboRIO Imaging Tool

2. Next, download the FRC WPILIB Suite (TOOLS ONLY) from the WPILib website.
    You can find the download like `here <https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html>`_.

    .. important:: 
        * Make sure to only install the tools, not the whole suite, as we do not program in Java or C++.
    
    This Suite will install a lot of software, but make sure to pin the following:
    
       * Shuffleboard

3. Next, download the Radio Configuration Tool from the WPIlib website.
    You can find the download link `here <https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/radio-programming.html>`_.
    
4. Next, Visit Mechanical Advantages Github to download AdvantageScope.
    You can find the download link `here <https://github.com/Mechanical-Advantage/AdvantageScope>`_.
    
    Follow the directions on the Github page to install the software.

5. Next, visit CTRE's website to download Pheonix Framework Installer.
    You can find the download link `here <https://store.ctr-electronics.com/software/>`_.
    
    .. note::

      If you have bought the Pheonix Tuner Pro license, you will need to sign in to your account.

6. Finally, visit Rev Robotics website to download the Rev Hardware Client.
    You can find the download link `here <https://docs.revrobotics.com/rev-hardware-client/>`_.
    
    

Software Setup:
---------------

Driver Station:
~~~~~~~~~~~~~~~

1. First, open the Driver Station, and select the "Setup" tab.
2. Switch the team number to our team number (Team 7407)

Radio Configuration:
~~~~~~~~~~~~~~~~~~~~

.. tab-set:: 

    .. tab-item:: For Practice
        :sync: For Practice

            1. Connect the radio to the computer using an ethernet cable. It must be powered on, but not connected to the robot.
            2. Open the Radio Configuration Utility.
            3. Enter the team number (7407) and click "Load Firmware".
            4. Watch it stand on business for a while.
            5. You're done!

    .. tab-item:: For Competition
        :sync: For Competition
    
          1. Locate and connect the radio to the selected Radio stations at the event using an ethernet cable. The Radio should be powered on, but not connected to the robot.
          2. Enter the team number (7407) and click "Load Firmware".
          3. Watch it stand on business for a while.
          4. You're done!

AdvantageScope:
~~~~~~~~~~~~~~~

1. Click on the "help" tab, and select 'Config'
2. Type in our team IP address (I forgor) and exit the program.
3. You're done!

CTR Pheonix Tuner:
~~~~~~~~~~~~~~~~~~

1. Open the program and enter the team IP address (I forgor) and click "Connect".
2. You're done!
