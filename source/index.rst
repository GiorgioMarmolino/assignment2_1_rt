.. Assignment2_1RT documentation master file, created by
   sphinx-quickstart on Fri Mar  7 16:42:13 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Assignment 2, Part 1 - Project Documentation
============================================
Welcome to the documentation of the first part of the second project related to the Research Track 1 course.
In this project, a mobile robot moves in an environment of a 3D simulator in presence of edges and obstacles 
(given by walls); the goal of the robot is to reach the target position sent by the user.

This project has been developed starting from the original package of prof. Recchiuto:

'Original repository: <https://github.com/CarmineD8/assignment_2_2024>'

Two nodes have been developed by me:
-first node implements an action client, allowing the user to set a target (x, y) or to cancel it. It uses 
the feedback/status of the action server to know when the target has been reached. The node also publishes 
the robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published 
on the topic /odom (odometry);
-second node implements a service node that, when called, returns the coordinates of the last target sent by 
the user;

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Introduzione
   Installazione
   Action_client_node
   Coordinate_service



Research Track 1: second assignment project documentation 
*********************************************************

Here is the documentation for the first part of the second project related to the Research Track 1 course.
SCRIVERE COSA FA IL PROGETTO


Indices
*******
 * :ref:`introduzione`
 * :ref:`installazione`
 * :ref:`action_client_node`
 * :ref:`coordinate_service`

---
.. _Introduzione:
Introduzione
============
Questa è la sezione introduttiva. **SCRIVI UN INTRO**

---
.. _Installazione:

Installazione
=============

Istruzioni su come installare il progetto.

---
.. _Action_client_node:
Action Client Node
==================
.. automodule:: scripts.action_client_node_A
   :imported-members:
   :members:
   :undoc-members:
   :show-inheritance:
---


.. _Coordinate_service:
Coordinate Service
==================
.. automodule:: scripts.coordinate_srv
   :imported-members:
   :members:
   :undoc-members:
   :show-inheritance: