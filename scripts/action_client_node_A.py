"""
.. module:: action_client_node_A
    
	    :platform: Unix
	    :synopsis: Python module for the action_client_node 
	    :author: Marmolino Giorgio  
    
    
This node implements an action client that allows the user to set the coordinates of a target position ([x, y] coordinates) 
that the mobile robot must reach. The user enters the target coordinates via keyboard input in the terminal, and the node 
sends these coordinates to the action server using the topic `/reaching_goal`.

Node functionalities:

	- Requests target coordinates from the user.
	- Sends the goal coordinates to the action server.
	- Allows the user to cancel the goal by pressing `"k"`.
	- Monitors the robot's position and velocity via the `/odom` topic.
	- Publishes position and velocity using the custom message type `PosVel` on the `/posVel` topic.

**Topics**:
	- *Subscribed:* `/odom` (to receive the robot's current state).
	- *Published:* `/posVel` (to broadcast the robot's position and velocity).


"""


#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Point, Pose, Twist, PoseStamped
from nav_msgs.msg import Odometry

import assignment2_1_rt
from assignment2_1_rt.srv import SentCoords
from assignment2_1_rt.msg import PosVel, PlanningAction
import actionlib
import actionlib.msg
from actionlib_msgs.msg import GoalStatus

import sys
import select
import time

# Global Variables
OdPose = Pose()
OdTwist = Twist()
pub_PsVl = rospy.Publisher("/posVel", PosVel, queue_size=10)
msg_PsVl = PosVel()  # Message to be published



def pos_client():
    """

    The main function of the action client node.

    This function initializes the ROS node, subscribes to the `/odom` topic to receive odometry data, 
    and establishes a connection to the action server at `/reaching_goal`.

    **Functionality**:
    
	    - Requests target coordinates from the user.
	    - Sends these coordinates as a goal to the action server.
	    - Waits for the robot to reach the goal or allows cancellation if the user presses `"k"`.
    
    A try-except block is used to handle incorrect input values or unexpected errors.

    :returns: None
    
    """
    
    rospy.init_node('bug_action_client')
    rospy.Subscriber("/odom", Odometry, odom_callback)  # Subscribe to odometry topic
    rate = rospy.Rate(10)
    act_pos = PoseStamped()

    client = actionlib.SimpleActionClient('/reaching_goal', assignment2_1_rt.msg.PlanningAction)
    client.wait_for_server()

    while not rospy.is_shutdown():
        time.sleep(3)  # Delay for cleaner terminal output
        print("\nEnter goal position as [x y] values:")

        try:
            act_pos.pose.position.x = float(input("\n X value: "))
            act_pos.pose.position.y = float(input("\n Y value: "))
            act_pos.pose.position.z = 0.0

            goal = assignment2_1_rt.msg.PlanningGoal(target_pose=act_pos)
            client.send_goal(goal)

            rospy.loginfo("Coordinates (%.1f, %.1f) sent | Press 'k' to cancel the goal." %
                          (act_pos.pose.position.x, act_pos.pose.position.y))

            while client.get_state() != actionlib.GoalStatus.SUCCEEDED:
                i, o, e = select.select([sys.stdin], [], [], 1.0)
                pos_callback()  # Publish position and velocity
                if i:
                    cancel = sys.stdin.readline().strip()
                    if cancel == 'k':
                        client.cancel_goal()
                        rospy.loginfo("Goal canceled.")
                        break

            if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
                rospy.loginfo("Robot has reached the target position.")

        except ValueError:
            rospy.logwarn("Invalid input - Please enter numerical values.")
        except Exception as err:
            rospy.logerr(f"Unexpected error: {err}")

        rate.sleep()


def pos_callback():

    """
     
    Transfers values from the `/odom` topic to the `/posVel` topic using a custom message.

    This function retrieves the robot's position and velocity from the global variables `OdPose` and `OdTwist`, 
    packages them into a `PosVel` message, and publishes them to `/posVel`.

    :returns: None
    
    """
    global pub_PsVl  # Publisher
    global OdPose, OdTwist  # Pose and twist from odometry 

    PsVl = PosVel()  # Define a PosVel message to be published
    PsVl.pos_x = OdPose.position.x
    PsVl.pos_y = OdPose.position.y
    PsVl.vel_x = OdTwist.linear.x
    PsVl.vel_z = OdTwist.angular.z
    pub_PsVl.publish(PsVl)


def odom_callback(msg_PsVl):

    """
    
    Callback function for the `/odom` topic.

    This function retrieves the robot's position and velocity from the odometry message and stores them 
    in global variables.

    :param msg_PsVl: An `Odometry` message containing the robot's position and velocity.
    :type msg_PsVl: nav_msgs.msg.Odometry
    :returns: None
    
    """
    global OdPose, OdTwist
    OdPose = msg_PsVl.pose.pose
    OdTwist = msg_PsVl.twist.twist


if __name__ == '__main__':
    time.sleep(12)
    pos_client()

