=========================
Operator Interface (OI)
=========================

The `OI.py` and `keymap.py` files in our repository collaboratively manage the operator interface, facilitating the mapping of controller inputs to specific robot commands. During a given season, keymap will be used to map certain controller inputs with commands, and OI will be used to determine which buttons were triggered.

Keymap Module
=============

The `keymap.py` module defines the controllers and their respective button mappings... 
The following is an example of a drivetrain keymap. There will be different keymap commands for each subsystem, and you can bind any button on an xbox controller.

- **Controllers:**
  
  - `DRIVER`: Assigned to port 0.
  
  - `OPERATOR`: Assigned to port 1.

- **Keymap:**
  
  - **Drivetrain:**
    
    - `DRIVE_X_AXIS`: Controls lateral movement.
    
    - `DRIVE_Y_AXIS`: Controls forward and backward movement.
    
    - `DRIVE_ROTATION_AXIS`: Controls rotational movement.
    
    - `RESET_GYRO`: Triggered by pressing the down direction on the D-pad.
    
    - `X_MODE`: Activated by pressing the 'X' button.
  
OI Module
=========

The `OI.py` module initializes the operator interface and maps the controls defined in `keymap.py` to specific commands: (This example is from the `7407-DriveCode-Crescendo` repository)

Controlling Keymap
------------------
OI allows you to check to see if a button is triggered. If it is, the function which the controller is binded to will be called.

By structuring the operator interface through the `OI.py` and `keymap.py` modules, developers can maintain a clear and organized mapping of controls, enhancing both the development process and the user experience during robot operation.