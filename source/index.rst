.. Assignment2_1RT documentation master file, created by
   sphinx-quickstart on Fri Mar 7 16:42:13 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Assignment 2, Part 1 - Project Documentation
============================================
Welcome to the documentation of the first part of the second project related to the Research Track 1 course.


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices
*******
* :ref:`Introduction`
* :ref:`Installation`
* :ref:`Action_client_node`
* :ref:`Coordinates_service`
* :ref:`Launch_file`
* :ref:`Message`
* :ref:`Service`
* :ref:`Running_the_project`



Research Track 1: Second Assignment Project Documentation
==========================================================



.. _Introduction:

Introduction
*************
Here is the documentation for the first part of the second project related to the Research Track 1 course. In this project, a mobile robot moves in an environment of a 3D simulator in presence of edges and obstacles (given by walls); the goal of the robot is to reach the target position sent by the user.

This project has been developed starting from the `original package <https://github.com/CarmineD8/assignment_2_2024/>`_ of Prof. Recchiuto.

Two nodes have been developed by me:

- **First node** implements an action client, allowing the user to set a target (x, y) or to cancel it. It uses 
  the feedback/status of the action server to know when the target has been reached. The node also publishes 
  the robot position and velocity as a custom message (x, y, vel_x, vel_z), by relying on the values published 
  on the topic `/odom` (odometry).
  
- **Second node** implements a service node that, when called, returns the coordinates of the last target sent by the user.

**Valutare di inserire eventuali immagini** parla dell'enviornment mettendo un immagine cose varie

.. _Installation:

Prerequisites
**************
Before executing the project you are required to: 

1. Install Gazebo, the 3D simulator for the ROS;

2. Install Rviz, a tool for ROS visualization that allows the user to view the simulated mobile robot model with all its sensors and related informations;
it is usefull for debug purposes;

3. Xterm;

4. python3, since the code is written in python3;

5. Robot Operating System (known as ROS);





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
	
	2. the second window is usefull whenever you want to check the goal sent to the action service, by using the command rosservice call /SentCoord
	
	3. the third window can be used to check the values published as a custom message on the topic /posVel; this can be done using the command


.. code-block:: bash

      rostopic echo /posVel
      



Node Descriptions
==================

.. _Action_client_node:

Action Client Node
*******************
.. automodule:: scripts.action_client_node_A
   :members:
   :undoc-members:
   :show-inheritance:

.. _Coordinates_service:

Coordinates Service
********************
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

The launch file also includes `sim_w1.launch`, which may start the simulator or other necessary components.



Messages and Services
======================

.. _Message:

PosVel.msg
***********

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



.. _Service:

SentCoords.srv
***************

This service has been defined in order to retrieve the target position.

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




