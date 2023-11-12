==================
File Structure
==================

the file structure for the robot code:

here is the file structure for the robot code:

.. .. uml:: 
    
..     title File Structure

..     folder Subsystems {
..         file subsystem.py
..     }
..     folder Sensors {
..         file sensor.py
..     }
..     folder Utils {
..         file util.py
..     }
..     folder Commands {
..         file command.py
..     }
..     folder OI {
..         file oi.py
..     }
..     folder Tests #Gold
..     file constants.py
..     file config.py
..     file robot.py #RoyalBlue
..     file robot_systems.py

..     subsystem.py -down-> robot_systems.py
..     robot_systems.py -down-> robot.py
..     subsystem.py -down-> command.py
..     util.py -down-> command.py
..     sensor.py -down-> command.py
..     command.py -down-> oi.py
..     robot_systems.py -> oi.py
..     command.py -down-> robot.py
..     oi.py -down-> robot.py


..     Subsystems -> Tests #Gold
..     Commands -> Tests #Gold
..     Sensors -> Tests #Gold
..     OI -down-> Tests #Gold
..     Utils -> Tests #Gold
..     robot_systems.py -right-> Tests #Gold

..     constants.py -down-> subsystem.py #Red
..     constants.py -down-> util.py #Red
..     constants.py -down-> sensor.py #Red

..     config.py -down-> subsystem.py #Green
..     config.py -down-> util.py #Green
..     config.py -down-> sensor.py #Green

...yeah, that's a lot of stuff. Let's break it down.



