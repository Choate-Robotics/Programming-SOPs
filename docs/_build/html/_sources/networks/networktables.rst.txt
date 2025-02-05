Networktables:
--------------

Networktables is a way for the RoboRIO to communicate with the driver station. It is used to send data to the driver station and to recieve data from the driver station. Networktables is used to send data such as the robot's position, the robot's speed, and the robot's angle. Networktables is also used to recieve data such as the joystick's position, the joystick's button presses, and the joystick's angle.

* We use Networktables to send data between other devices on the robot, the RoboRIO, and the driver station (EX: Limelight)

* Networktables is a Pub/Sub system, meaning that devices can automatically recieve data from other devices without having to request it.

* [Networktables Documentation](http://robotpy.readthedocs.io/en/stable/guide/nt.html)

.. graphviz:: 

    digraph{
        "Networktables" -> "Raspberry Pi";
        "Networktables" -> "RoboRIO";
        "Networktables" -> "Driver Station";
        "Networktables" -> "Limelight";
    }

Communicating from the RoboRIO:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To communicate with the networktable system, you must first instance the networktable object. This is done by using the following code:

.. code-block:: python

    import ntcore

    table = ntcore.NetworkTables.NetworkTableInstance.getTable("tablename")

.. note::
    The ``tablename`` is the name of the table you want to communicate with. The table name is usually the name of the robot.

To send data to the networktable, you must use the following code:

.. code-block:: python

    table.putNumber("key", value)

.. note::
    The ``key`` is the name of the data you want to send. The ``value`` is the data you want to send.

To recieve data from the networktable, you must use the following code:

.. code-block:: python

    value = table.getNumber("key", default)

.. note::
    The ``key`` is the name of the data you want to recieve. The ``default`` is the value that will be returned if the ``key`` does not exist.

If you want to start a Publisher, you must use the following code:

.. code-block:: python

    table = ntcore.NetworkTables.getTable("tablename")
    # in progress

This will start a publisher that will send data to the networktable.

