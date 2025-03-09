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


OdPose = Pose()
OdTwist = Twist()
pub_PsVl = rospy.Publisher("/posVel", PosVel, queue_size = 10)
msg_PsVl = PosVel()# message to be published

'''
Action client - Node description:

This node implements an action client that allow the user to set the coordinates of a target position ([x y] coordinates) that the 
mobile robot has to reach; going deeper, writing with the keyboard on the terminal line, the user send to the action 
server the new coordinates by the topic '/reaching_goal'. Once the node is running, a message will be displayed 
asking the user to send coordinates of the target; once the message is sent, the user is allowed to cancel the 
sent goal by sending a 'k' until the robot reach the target (this is implemented relying on the feedback/status 
of the action server) ;otherwise the robot will work until it reach the target. Since the node is required to 
publish as a custom message the position and velocuty of the robot relying on the values published on the 
topic /odom, inside of it we can find:
- a subscriber to the topic /odom
- a publisher on the topic /posVel
- function pos_callback() implemented in order to take values from the topic /odom and publish it on the topic /posVel

'''

def pos_client(): #this works as the main function

    '''
    This is the main function of the *action client node*;
    '''
    





    
    rospy.init_node('bug_action_client')
    rospy.Subscriber("/odom", Odometry, odom_callback)#to read odometry values
    rate = rospy.Rate(10)
    act_pos = PoseStamped()

    #as standard from launch file parameters: #not eequired
    #act_pos.pose.position.x = rospy.get_param('target_x')
    #act_pos.pose.position.y = rospy.get_param('target_y')
    #act_pos.pose.position.z = 0.0


    client = actionlib.SimpleActionClient('/reaching_goal', assignment2_1_rt.msg.PlanningAction)
    client.wait_for_server()

    
    while not rospy.is_shutdown():
        time.sleep(3) #used for a clean output on the terminal
        print("\n enter goal position as [x y] values: ")
        try:
            act_pos.pose.position.x = float(input("\n X value: "))
            act_pos.pose.position.y = float(input("\n Y value: "))
            act_pos.pose.position.z = 0.0
            goal = assignment2_1_rt.msg.PlanningGoal(target_pose=act_pos)
            client.send_goal(goal)
            rospy.loginfo("Coordinates (%.1f, %.1f) sent | Press 'k' to cancel the sent target coordinates: "%(act_pos.pose.position.x, act_pos.pose.position.y ))
            
            while(client.get_state() != actionlib.GoalStatus.SUCCEEDED):
                i, o, e = select.select([sys.stdin], [], [], 1.0)
                pos_callback()
                if(i):
                    cancel = sys.stdin.readline().strip()
                    if cancel == 'k':
                        client.cancel_goal()
                        #rospy.loginfo("Goal deletion: confirmed") #log already exist
                        break
            
            if(client.get_state() == actionlib.GoalStatus.SUCCEEDED):
                rospy.loginfo("Robot has been reached the target position")

        except ValueError:
            print("Invalid input - Please enter a number")
        except Exception as err:
            print(f"Unexpected error: {err}")
        rate.sleep()


        
def pos_callback():
        global pub_PsVl #publisher
        global OdPose, OdTwist  #pose and twist from odometry 

        PsVl = PosVel() #define a PosVel var to be used to send the custom message
        PsVl.pos_x = OdPose.position.x
        PsVl.pos_y = OdPose.position.y
        PsVl.vel_x = OdTwist.linear.x
        PsVl.vel_z = OdTwist.angular.z
        pub_PsVl.publish(PsVl)
        

def odom_callback(msg_PsVl):
    global OdPose, OdTwist
    OdPose = msg_PsVl.pose.pose
    OdTwist = msg_PsVl.twist.twist

if __name__ == '__main__':
    time.sleep(12)
    pos_client()
