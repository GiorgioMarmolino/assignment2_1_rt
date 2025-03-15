.. Assignment2_1RT documentation master file, created by
   sphinx-quickstart on Fri Mar 7 16:42:13 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Assignment 2, Part 1 - Project Documentation
============================================
Welcome to the documentation of the first part of the second project related to the Research Track 1 course.


.. toctree::
   :maxdepth: 4
   :caption: Contents:


Indices
=======
* :ref:`Introduction`
* :ref:`Installation`
* :ref:`Running_the_project`
* :ref:`Package_description`
* :ref:`Package_dependencies`
* :ref:`Node_description`
* :ref:`Launch_file`
* :ref:`Messages,_services_and_actions`




Research Track 1: Second Assignment Project Documentation
=========================================================


.. _Introduction:

Introduction
************
Here is the documentation for the first part of the second project related to the Research Track 1 course. In this project, a mobile robot moves in an environment of a 3D simulator in presence of edges and obstacles (given by walls); the goal of the robot is to reach the target position sent by the user. Given by the original package, the robot has been projected in order to follow a path according to the presence of walls; dedicated nodes developed by Prof. Recchiuto in the `original package <https://github.com/CarmineD8/assignment_2_2024/>`_ are used in order to reach the target position and follow the walls when they are detected trought sensors. Click to this `link <https://github.com/GiorgioMarmolino/assignment2_1_rt/>`_ to download the whole project.

.. container:: images-row

   .. figure:: images/Path2d.JPG
      :alt: Example of robot path to reach the target position.
      :align: left
      :figwidth: 40%

   .. figure:: images/SimulationEnvironment.JPG
      :alt: 3D simulation environment.
      :align: left
      :figwidth: 50%
      




Two nodes have been developed by me:

- **First node** implements an action client, allowing the user to set a target (x, y) or to cancel it. It uses 
  the feedback/status of the action server to know when the target has been reached. The node also publishes 
  the robot position and velocity as a custom message (x, y, vel_x, vel_z), by relying on the values published 
  on the topic `/odom` (odometry);
  
- **Second node** implements a service node that, when called, returns the coordinates of the last target sent by the user, retrieving values from the launch file    parameters;


.. _Installation:

Prerequisites
**************

Before executing the project, you are required to install these tools, that are essential for the smooth execution and operation of the project:

1. **Gazebo**: A 3D simulator for ROS that allows you to simulate robotic environments, test algorithms, and evaluate robot behavior in a virtual setting.

2. **Rviz**: A powerful tool for ROS visualization that enables users to view the simulated mobile robot model along with its sensors, status, and related information. Rviz is particularly useful for debugging, monitoring sensor data, and inspecting the robot's environment.

3. **Python 3**: Required because the code is written in Python 3, which includes important features and lbraries for robot control, data processing, and interaction with ROS nodes.

4. **Robot Operating System (ROS)**: A flexible framework for writing robot software that provides a collection of tools, libraries, and conventions to simplify the development of complex robot behavior. ROS is essential for managing the communication between different parts of the system, including sensors, actuators, and algorithms.


.. _Running_the_project:

Running the project
********************

This section is about hot to install and start the simulation system. After cloning this repository into your *src/* folder of your **ROS1 workspace**:


1. **Clone the Git repository**: To obtain the source code, run the following command:  

   .. code-block:: bash

      git clone https://github.com/GiorgioMarmolino/assignment2_1_rt

2. **Compile the package in ROS**: Navigate to the main folder of your ROS workspace and build the package:  

   .. code-block:: bash

      catkin_make --only-pkg-with-deps assignment2_1_rt

3. **Launch the project**: Once the compilation is complete, run the launch file to start the project:  

   .. code-block:: bash

      roslaunch assignment2_1_rt assignment1.launch



To manage the project and see it all, it is not mandatory but it is higly recommended to open more windows:


	1. in the first window execute the roslaunch command: here you will use this window to send commands about the target position or to cancel the goal sent to the action service;
	
	2. the second window is usefull whenever you want to check the goal sent to the action service, by using the command rosservice call */SentCoord*;
	
	3. the third window can be used to check the values published as a custom message on the topic */posVel*; this can be done using the command;


.. code-block:: bash

      rostopic echo /posVel
   
   
.. _Package_description:
   
Package description
===================

This ROS package provides a complete environment for developing and testing autonomous navigation algorithms. The robot can be controlled via ROS services and pre-defined action servers, while the Gazebo simulation ensures realistic behavior. Additionally, RViz integration allows real-time monitoring of the robot's position and actions. Since the package is designed for simulation and control of a mobile robot, **Gazebo** is for physics simulation and **RViz** is used for visualization. The package structure is organized into multiple directories to separate configuration files, ROS nodes, and simulation assets.

.. figure:: images/packageStructure.JPG
      :alt: 3D simulation environment.
      :align: center


Structure Overview
******************

- **Configuration and Build Files**
  
  - ``CMakeLists.txt``, ``package.xml``: Required files for package configuration and compilation.
  - ``Doxyfile.in``, ``Makefile``: Used for automatic documentation generation.

- **Custom Messages, Services, and Actions**
  
  - ``msg/PosVel.msg``: Defines a custom ROS message for inter-node communication.
  - ``srv/SentCoords.srv``: Defines a ROS service for handling coordinate data.
  - ``action/Planning.action``: Defines an action for long-term tasks, such as movement control.

- **RViz Configuration Files**
  
  - ``config/sim.rviz``, ``config/sim2.rviz``: Configuration files for RViz visualization.

- **Launch Files**
  
  - ``launch/assignment1.launch``, ``launch/sim_w1.launch``: ROS launch files that start the simulation and required nodes.

- **ROS Nodes (Python Scripts)**
  
  The ``scripts/`` directory contains various ROS nodes:

  - ``action_client_node_A.py``: Action client node for executing ``Planning.action``.
  - ``bug_as.py``: This script implements a ROS action that allows a mobile robot to reach a target position while avoiding obstacles when necessary.
  - ``coordinates_srv.py``, ``go_to_point_service.py``, ``wall_follow_service.py``: ROS services for robot control, including waypoint navigation, wall-following behavior and information retrieving.

- **Gazebo Simulation Files**
  
  - ``urdf/robot2_laser.gazebo``, ``urdf/robot2_laser.xacro``: URDF model files defining the robot for Gazebo simulation.
  - ``world/assignment.world``: Defines the simulated environment for testing the robot.


.. _Package_dependencies:

Package dependencies
====================

This package relies on multiple ROS components for navigation, messaging, and action management. The dependencies are defined in both the ``package.xml`` and ``CMakeLists.txt`` files.

Required Dependencies
***********************

The following ROS packages are required for building and running this package:

- **Core ROS Libraries**:
	  - ``roscpp`` : C++ client library for ROS.
	  - ``rospy`` : Python client library for ROS.
	  - ``catkin`` : ROS build system.

- **Messaging and Services**:
	  - ``std_msgs`` :Standard ROS message types (e.g., strings, integers, booleans).
	  - ``std_srvs`` : Standard ROS service definitions.
	  - ``message_generation`` : Required for generating custom messages, services, and actions.
	  - ``message_runtime`` : Allows the use of generated messages in runtime.

- **Navigation and Coordinate Transformations**:
	  - ``geometry_msgs`` : Messages for positions, velocities, and transformations.
	  - ``nav_msgs`` : Provides message types for navigation, such as odometry and path planning.
	  - ``tf`` : Handles transformations between coordinate frames.

- **Action and Communication Services**:
	  - ``actionlib`` : ROS library for implementing action servers and clients.
	  - ``actionlib_msgs`` : Standard message definitions for ROS actions.

- **Sensor Integration**:
  	  - ``sensor_msgs`` : Defines messages for sensor data (e.g., laser scanners, cameras, IMUs).

Configuration Files
*********************

The dependencies are declared in the following files:

- **`package.xml`**: Specifies build-time and run-time dependencies using `<depend>` tags.
- **`CMakeLists.txt`**: Defines dependencies using ``find_package(catkin REQUIRED COMPONENTS ...)``.

Installation
***************

To ensure all dependencies are installed, run:

.. code-block:: bash

   rosdep install --from-paths src --ignore-src -r -y

This command automatically installs missing dependencies based on the ``package.xml`` file.





.. _Node_description:

Node Descriptions
=================



Action Client Node
********************
.. automodule:: scripts.action_client_node_A
   :members:
   :undoc-members:
   :show-inheritance:



Coordinates Service
*********************
.. automodule:: scripts.coordinates_srv
   :members:
   :undoc-members:
   :show-inheritance:
   

.. _launch_file:

ROS Launch File
===============

This launch file starts several nodes from the `assignment2_1_rt` package.  
It also includes another launch file, `sim_w1.launch`, and sets some initial parameters.

**Launch file content:**

.. code-block:: xml

    <?xml version="1.0"?>
    <launch>
        <include file="$(find assignment2_1_rt)/launch/sim_w1.launch" />
        <param name="target_x" value="0.0" />
        <param name="target_y" value="1.0" />
        <node pkg="assignment2_1_rt" type="wall_follow_service.py" name="wall_follower" />
        <node pkg="assignment2_1_rt" type="go_to_point_service.py" name="go_to_point"  />
        <node pkg="assignment2_1_rt" type="bug_as.py" name="bug_action_service" output="screen" />

        <node pkg="assignment2_1_rt" type="action_client_node_A.py" name="bug_action_client" output="screen" />
        <node pkg="assignment2_1_rt" type="coordinates_srv.py" name="coordinates_service" output="screen" />
    </launch>

**Node descriptions:**
	- **wall_follower**: Node that follows walls.
	- **go_to_point**: Implements a service to move the robot toward a point.
	- **bug_action_service**: Implements an action for the robot's movement.
	- **bug_action_client**: Client to interact with the navigation service.
	- **coordinates_service**: Service that provides the coordinates of the last target.

**Initial parameters:**
	- `target_x = 0.0`
	- `target_y = 1.0`

The launch file also includes `sim_w1.launch`, which may start the simulator and other necessary components (given by the original package of the assignment).



.. _Messages,_services_and_actions:

Messages, services and actions
==============================



PosVel.msg
**********

This message is used in order to represent a 2D position in space (so altitude excluded) and a velocity.


**Message definition:**

.. code-block:: text

    float32 pos_x 
    float32 pos_y
    float32 vel_x
    float32 vel_z

**Fields:**
	- **pos_x**: *x*-axis robot position;
	- **pos_y**: *y*-axis robot position;
	- **vel_x**: *x*-axis robot linear velocity;
	- **vel_z**: *z*-axis robot angular velocity;





SentCoords.srv
**************

This service has been defined in order to retrieve the target position from the target position parameters inside the launch file.

**Service definition:**

.. code-block:: text

    ---
    string Info
    float32 Pos_x_sent
    float32 Pos_y_sent


**Fields:**

- **Request**: No parameters;
- **Response**:
	- **x**: *x*-axis target position;
	- **y**: *y*-axis target position;


Planning.action
***************

The *Planning* action is designed to move a robot to a target position defined by a **PoseStamped**. The action accepts a target pose, and during execution, provides periodic feedback on the robot's current position, along with the movement status.

- **Goal**

	- *target_pose* (``geometry_msgs/PoseStamped``): The target position the robot should reach, represented as a **PoseStamped** message. It includes the position (x, y, z) and orientation (roll, pitch, yaw) of the robot relative to a reference frame.

- **Feedback**
	- *actual_pose* (``geometry_msgs/Pose``): The current position of the robot, which provides periodic updates during the movement. The **Pose** message includes the position (x, y, z) and orientation (roll, pitch, yaw) relative to the robot's reference frame.

- **Result**

	- *stat* (``string``): A string indicating the status of the operation. Possible values include:
	
		  - `"success"`: The robot successfully reached the target position.
		  - `"failure"`: The robot failed to reach the target position (e.g., due to movement errors or unexpected obstacles).
	 	  - `"in_progress"`: The operation is still in progress, and the robot is moving toward the target position.

.. raw:: html

	<h4>Usage</h4>

When this action is invoked, the **target_pose** represents the desired destination for the robot. The feedback (``actual_pose``) will be periodically sent to monitor the robot's current position while moving toward the goal. At the end of the action, the result (``stat``) will indicate whether the operation was successfully completed or not.

.. raw:: html

	<h4>References</h4>

See the ``geometry_msgs/PoseStamped`` and ``geometry_msgs/Pose`` message types for more details on the structure of the target and actual poses.



    



