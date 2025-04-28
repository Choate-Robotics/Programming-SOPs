Logging Procedures Thoughts
===========================

- We should setup logging to happen to the USB Stick automatically.
- We should review the logs after every match.

  - Were there any warnings?
  - Are we reaching set points quickly?
  - How is our odometry?

    Comparing Odometry with Match Video in AdvantageScope
    ----------------------------------------------------

    **AdvantageScope** allows you to overlay your robot's **odometry data** with actual **match video**. This is a powerful way to verify how accurate your robot's pose estimation is compared to its real-world movement.

Preparation for the creation of log files
=========================================

Some preparation has to be done to make sure that `.wpilog` file will be on the USB stick connected to the Roborio.

- The USB stick must be a FAT32 filesystem.
- There needs to be a directory in the home directory named `logs`.
- The robot should be turned off before the USB stick is removed.

The logger that is used needs some particular setup as well.

- ``DriveStation.startDataLog`` needs to be called to record the joystick data.
- If a ``deploy`` folder has been put in the robot code, and a ``deploy.json`` has been created, then the git branch name and commit id can be recorded in the log using the ``getDeployData`` method.

Steps to Compare Odometry with Match Video in AdvantageScope
============================================================

1. Record Odometry Data During the Match
----------------------------------------

Ensure that your robot is logging its odometry data to a `.wpilog` file. This usually involves publishing the robot's pose to **NetworkTables**.

.. code-block:: python

    import wpilib

    class MyRobot(wpilib.TimedRobot):
        def robotInit(self):
            self.field = wpilib.Field2d()
            wpilib.SmartDashboard.putData("Field", self.field)

        def robotPeriodic(self):
            # Assuming you have an odometry object tracking robot pose
            pose = self.odometry.getPose()
            self.field.setRobotPose(pose)

This will log odometry data that AdvantageScope can visualize.

2. Record or Obtain the Match Video
-----------------------------------

You can use:

- **Official FRC match footage** from sources like **The Blue Alliance**.
- **Custom recordings** from team cameras.
- **Field overlays** from field cameras.

Ensure that the video includes:

- **Clear views of the robot**.
- **Match timer visible**, if possible (helps with synchronization).

3. Load the `.wpilog` File into AdvantageScope
----------------------------------------------

1. **Open AdvantageScope**.
2. Go to **File > Open Log File**.
3. Select your **`.wpilog` file** containing odometry data.
4. Add a **Field2d** visualization to see the robot's path.

4. Load the Match Video into AdvantageScope
-------------------------------------------

AdvantageScope supports **synchronized video playback** alongside telemetry data.

**Steps to Load Video:**

1. Go to **Video** in the sidebar.
2. Click **Add Video** and select your **match video file** (`.mp4`, `.mov`, etc.).
3. The video will appear in a **side-by-side view** with your odometry data.

5. Synchronize the Video with the Odometry Data
-----------------------------------------------

To compare accurately, you need to **synchronize the video timeline** with your robot's telemetry.

**Synchronization Tips:**

- **Match Timers**: Use the **match start buzzer** or **field timer** visible in the video to align timestamps.
- **Distinct Events**: Look for **unique actions** (e.g., robot crossing a line, shooting a game piece) to sync the odometry with the video.

**Adjusting Sync in AdvantageScope:**

1. Use the **video timeline** to align the **start of autonomous** or **teleop** with your log data.
2. Adjust the **video offset** under the video settings if needed.

6. Analyze the Odometry vs. Video
---------------------------------

Now you can **compare your robot's estimated path (odometry)** with its **actual path in the video**.

- Look for **drift** in odometry over time.
- Verify if **swerve modules**, **gyro**, or **encoders** need recalibration.
- Identify discrepancies in **pose estimation algorithms**.

Why This is Useful
==================

1. Make sure that button presses and actions of the robot align.
2. Check performance of the swerve modules.
3. **Odometry Calibration**: Helps identify if the robot's sensors (gyros, encoders) are causing drift.
4. **Autonomous Debugging**: Check if the robot follows expected paths during autonomous.
5. **Sensor Fusion Tuning**: Compare pure odometry to odometry enhanced with **vision systems** (e.g., AprilTags).
