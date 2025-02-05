==================
Java Auto Example and Instructions
==================

Here is a code sample with how to make a basic auto in Java. This is for a tank drive robot, and it will drive forward for two seconds to get points from moving. Make sure to reconfigure the motors in this file to yours which are used in your subsystems.

.. code-block:: console
    :linenos:
   
    package frc.robot;

    import edu.wpi.first.wpilibj.TimedRobot;
    import edu.wpi.first.wpilibj.motorcontrol.PWMSparkMax;
    import edu.wpi.first.wpilibj.drive.DifferentialDrive;
    import edu.wpi.first.wpilibj.Timer;

    public class Robot extends TimedRobot {
        private final PWMSparkMax leftMotor = new PWMSparkMax(0);  
        private final PWMSparkMax rightMotor = new PWMSparkMax(1)
        private final DifferentialDrive drive = new DifferentialDrive(leftMotor, rightMotor);
        private final Timer timer = new Timer();

        @Override
        public void autonomousInit() {
            timer.reset();
            timer.start();
        }

        @Override
        public void autonomousPeriodic() {
            if (timer.get() < 2.0) {  // Move forward for 2 seconds
                drive.tankDrive(0.5, 0.5);  // 50% speed forward
            } else {
                drive.stopMotor();  // Stop after 2 seconds
            }
        }
    }
