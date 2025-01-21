=========================
Operator Interface (OI)
=========================

The `OI.py` and `keymap.py` modules in the `7407-DriveCode-Reefscape` repository collaboratively manage the operator interface, facilitating the mapping of controller inputs to specific robot commands. This structured approach ensures intuitive and efficient control during robot operation.

Keymap Module
=============

The `keymap.py` module defines the controllers and their respective button mappings:

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
  
  - **Elevator:**
    
    - `ELEVATOR_HIGH`: Activated by pressing the 'Y' button.
    
    - `ELEVATOR_MID`: Activated by pressing the 'B' button.
    
    - `ELEVATOR_LOW`: Activated by pressing the 'A' button.
    
    - `AMP`: Activated by pressing the 'X' button.
  
  - **Intake:**
    
    - `INTAKE_IN`: Triggered by pressing the right trigger beyond 40% threshold.
    
    - `INTAKE_OUT`: Triggered by pressing the left trigger beyond 40% threshold.
    
    - `AUTO_INTAKE`: Triggered by pressing the left trigger beyond 40% threshold on the driver controller.
  
  - **Shooter:**
    
    - `AIM`: Triggered by pressing the right trigger beyond 40% threshold.
    
    - `STATIC_FEED_SHOT`: Activated by pressing the left bumper.
    
    - `SET_WRIST_SUBWOOFER`: Triggered by pressing the right direction on the D-pad.
    
    - `ENABLE_AIM_WRIST_OPERATOR`: Triggered by pressing the left direction on the D-pad.
    
    - `FLYWHEEL_MANUAL_REVERSE`: Activated by pressing the right stick.
    
    - `AMP`: Activated by pressing the right bumper.
    
    - `FEED_SHOT`: Activated by pressing the 'B' button.
  
  - **Feeder:**
    
    - `FEED`: Activated by pressing the right bumper.
    
    - `UNFEED`: Activated by pressing the left bumper.
    
    - `DUMP_NOTE`: Activated by pressing the 'A' button.
    
    - `FEED_NOTE_FLYWHEEL`: Triggered by moving the left joystick upward beyond 40% threshold.
    
    - `SOURCE_FEED`: Activated by pressing the 'Start' button.
  
  - **Climb:**
    
    - `CLIMB_UP`: Activated by pressing the 'Select' button.
    
    - `CLIMB_DOWN`: Activated by pressing the 'Start' button.
    
    - `TRAP`: Triggered by pressing the up direction on the D-pad.
    
    - `UNDO_CLIMB_UP`: Triggered by pressing the down direction on the D-pad.

OI Module
=========

The `OI.py` module initializes the operator interface and maps the controls defined in `keymap.py` to specific commands: (This example is from the `7407-DriveCode-Crescendo` repository)

- **Initialization:**
  
  .. code-block:: python
  
     class OI:
         @staticmethod
         def init() -> None:
             log.info("Initializing OI...")

- **Control Mapping:**
  
  .. code-block:: python
  
     @staticmethod
     def map_controls():
         log.info("Mapping controls...")
         Keymap.Drivetrain.RESET_GYRO.onTrue(
             command.DrivetrainZero(Robot.drivetrain)
         ).onFalse(
             command.DriveSwerveCustom(Robot.drivetrain)
         )
         
         Keymap.Shooter.AIM.and_(
             lambda: not states.flywheel_state == states.FlywheelState.amping
         ).whileTrue(
             command.DriveSwerveAim(Robot.drivetrain, Field.calculations)
         ).onFalse(
             command.DriveSwerveCustom(Robot.drivetrain)
         )
         
         # Additional control mappings...

This setup ensures that each controller input is associated with the appropriate command, facilitating seamless robot operation.

By structuring the operator interface through the `OI.py` and `keymap.py` modules, developers can maintain a clear and organized mapping of controls, enhancing both the development process and the user experience during robot operation.