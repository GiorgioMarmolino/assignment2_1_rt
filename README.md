### RESEARCH TRACK - ASSIGNMENT 2 "3D MOBILE ROBOT MOTION PLANNING"

Made by: Marmolino Giorgio
a.y. 2024/2025
Project fully developed in python3

(previous assignment has been developed in C++)

## Project introduction
In this project, a mobile robot moves in an environment of a 3D simulator in presence of edges and obstacles (given by walls); the goal of the robot is to reach the target position sent by the user.

This project has been developed starting from the original package of prof. Recchiuto:

https://github.com/CarmineD8/assignment_2_2024

Two nodes have been developed by me:
-first node implements an action client, allowing the user to set a target (x, y) or to cancel it. It uses the feedback/status of the action server to know when the target has been reached. The node also publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the topic /odom (odometry);

-second node implements a service node that, when called, returns the coordinates of the last target sent by the user;

## Node descriptions

# First node: action client

This node implements an action client that allow the user to set the coordinates of a target position that the mobile robot has to reach; going deeper, writing with the keyboard on the terminal line, the user send to the action server the new coordinates by the topic '/reaching_goal'. Once the node is running, a message will be displayed asking the user to send coordinates of the target; once the message is sent, the user is allowed to cancel the sent goal by sending a 'k' until the robot reach the target (this is implemented relying on the feedback/status of the action server) ;otherwise the robot will work until it reach the target. Since the node is required to publish as a custom message the position and velocuty of the robot relying on the values published on the topic /odom, inside of it we can find:
- a subscriber to the topic /odom
- a publisher on the topic /posVel
- function pos_callback() implemented in order to take values from the topic /odom and publish it on the topic /posVel

# Second node: service node
This node is a service node, so it means that it implements a communication of type request/response; this node use the SentCoords service (inside the folder srv we can find SentCoords.srv); in detail this service is composed only by the response part since it is required to return two values related to the last target position coordinates sent by the user, and there isn't any client that makes a request. The .srv response part is composed of a message (so a string) and two float32 values; for calling the service it is sufficient to use the command:

rosservice call /SentCoord

and it will return:

Info:	""Last target sent coordinates: "
Pos_x_sent: [value]
Pos_y_sent: [value]

## Prerequisites
Before executing the project you are required to: 
1) Install Gazebo, the 3D simulator for the ROS;
2) Install Rviz, a tool for ROS visualization that allows the user to view the simulated mobile robot model with all its sensors and related informations; it is usefull for debug purposes;
3) Xterm;
4) python3, since the code is written in python3;
5) Robot Operating System (known as ROS);



## Running the project
After cloning this repository into your src/ folder of your ROS1 workspace:
```bash
git clone https://github.com/GiorgioMarmolino/assignment2_1_rt
```
go back in the main folder of your ROS-WS and build this package:
```bash
catkin_make --only-pkg-with-deps assignment2_1_rt
```
and launch the project using the launch file:
```bash
roslaunch assignment2_1_rt assignment1.launch
```

To manage the project and see it all, it is not mandatory but it is higly recommended to open more windows:
1) in the first window execute the roslaunch command: here you will use this window to send commands about the target position or to cancel the goal sent to the action service;
2) the second window is usefull whenever you want to check the goal sent to the action service, by using the command rosservice call /SentCoord
3) the third window can be used to check the values published as a custom message on the topic /posVel; this can be done using the command

```bash
rostopic echo /posVel
```