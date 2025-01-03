
#! /usr/bin/env python


import rospy
from geometry_msgs.msg import Point, Pose, Twist
from nav_msgs.msg import Odometry
from srv import SentCoords
from msg import PosVel
import actionlib
import actionlib.msg
import sys

from __future__ import print_function
import select


#from nav_msgs.msg import Odometry
#from actionlib_msgs.msg import GoalStatus

pub_PsVl = rospy.publisher("/posVel", PosVel, queue_size = 10)

'''
NODE DESCRIPTION:

The client waits for the user to enter a valid target position for the robot given by [x y] coordinates;
once the goal is sent, the user is allowed to cancel the sent goal pressing 'k' in the terminal command line;
if the user doesn't cancel the goal sent, the system will work without interruptions until the target position
is reached; once the target position is reached, the node will display a message confirming the goal.
'''



def callback_pos(msg): # callback used to publish values of pos and vel of robot, based on odomoetry values
    PsVl = PosVel()
    PsVl.x = msg.pose.pose.position.x
    PsVl.y = msg.pose.pose.position.y
    PsVl.vx = msg.twist.twist.linear.x
    PsVl.vz = msg.twist.twist.angular.z
    pub_PsVl.publish(PsVl)

def pos_client():
    # Creates the SimpleActionClient, passing the type of the action
    
    client = actionlib.SimpleActionClient('reached_target', assignment2_1_rt.msg.PlanningAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = assignment2_1_rt.msg.PlanningGoal(order=20)

    while not rospy.is_shutdown():
        rospy.loginfo("\n enter goal position as [x y] values: ")
        
        goal.target_pose.pose.position.x = float(input(''))
        goal.target_pose.pose.position.y = float(input(''))
        client.send_goal(goal) #send goal to the action server

        #then if the situation requires the target cancelation:
        print("Press 'k' to cancel the sent target coordinates: ")
        while(client.get_state() != actionlib.GoalAtatus.SUCCEEDED):
            i, o, e = select.select( [sys.stdin], [], [], 1.0 )
            if (i): #if there is input from terminal
                cancel = sys.stdin.readline().strip()
                if cancel == 'k':
                    client.cancel_goal()
                    print("Goal deletion: confirmed")
                    break
        
        if(client.get_state() == actionlib.GoalStatus.SUCCEEDED):
            print("Robot has been reached the target position")


if __name__ == '__main__':
    try:
        rospy.init_node('action_client_node_py')
        rospy.subscriber("/odom", Odometry, callback_pos) #to read [x y vx wz] values
        pos_client()
    except rospy.ROSInterruptException:
        print("Failed in execution: program interrupted before completion", file=sys.stderr)
