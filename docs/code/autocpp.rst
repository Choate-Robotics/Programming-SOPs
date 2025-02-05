==================
C++ Auto Example and Instructions
==================

Here is a code sample for how to make an auto in C++. Keep in mind, added files and variables such as the drivetrain 
will need to be imported from your codebase. Also, make sure to change the functions in our example code 
to similar ones in your codebase.

This sample was influenced by Team 1771's 2022 codebase.

.. code-block:: cpp
    :linenos:

    #include "Auton.hpp"
    #include "DriveTrain.hpp"
    #include "Intake.hpp"

    #include <units/angle.h>
    #include <units/time.h>
    #include <frc/Timer.h>
    #include <frc/smartdashboard/SendableChooser.h>
    #include <frc/smartdashboard/SmartDashboard.h>

    #include <thread>
    #include <functional>

    static frc::SendableChooser<std::function<void()>> auton_selector;

    void sleep()
    {
        std::this_thread::sleep_for(10ms);
    }

    void driveStraightFor(double velocity_percent, units::degree_t desired_CCW_rot, units::second_t time)
    {
        frc::Timer timer;
        timer.Start();

        while (!timer.HasElapsed(time))
        {
            DriveTrain::driveStraight(velocity_percent, desired_CCW_rot);
            sleep();
        }

        DriveTrain::stop();
    }