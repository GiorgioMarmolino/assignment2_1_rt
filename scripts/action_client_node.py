#! /usr/bin/env python


import rospy
from geometry_msgs.msg import Point, Pose, Twist
from sensors_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from assignment2_1_rt.srv import SentCoords
from assignment2_1_rt.msg import PosVel, PlanningAction
import actionlib
import actionlib.msg
imposrt actionlib_msgs.msg import GoalStatus
import sys
import select


#from nav_msgs.msg import Odometry
#from actionlib_msgs.msg import GoalStatus

pub_PsVl = rospy.Publisher("/posVel", PosVel, queue_size = 10)


'''
NODE DESCRIPTION:

The client waits for the user to enter a valid target position for the robot given by [x y] coordinates;
once the goal is sent, the user is allowed to cancel the sent goal pressing 'k' in the terminal command line;
if the user doesn't cancel the goal sent, the system will work without interruptions until the target position
is reached; once the target position is reached, the node will display a message confirming the goal.
'''



def callback_pos(msg): # callback used to publish values of pos and vel of robot, based on odomoetry values
    global pub_PsVl
    PsVl = PosVel()
    PsVl.pos_x = msg.pose.pose.position.x
    PsVl.pos_y = msg.pose.pose.position.y
    PsVl.vel_x = msg.twist.twist.linear.x
    PsVl.vel_z = msg.twist.twist.angular.z
    pub_PsVl.publish(PsVl)

def pos_client():
       
    client = actionlib.SimpleActionClient('reached_target', PlanningAction)
    client.wait_for_server()

    goal = assignment2_1_rt.msg.PlanningGoal(order=20)




    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("\n enter goal position as [x y] values: ")
        
        goal.target_pose.pose.position.x = float(input("X value: "))
        goal.target_pose.pose.position.y = float(input('Y value: '))
        client.send_goal(goal) #send goal to the action server

        #then if the situation requires the target cancelation:
        cancel = input("Press 'k' to cancel the sent target coordinates: ")
        while(client.get_state() != actionlib.GoalAtatus.SUCCEEDED):
            if cancel == 'k':
                    client.cancel_goal()
                    rospy.loginfo("Goal deletion: confirmed")
                    break
        
        if(client.get_state() == actionlib.GoalStatus.SUCCEEDED):
            rospy.loginfo("Robot has been reached the target position")
        rate.sleep()

if __name__ == '__main__':
    try:
        rospy.init_node('bug_action_client')
        rospy.Subscriber("/odom", Odometry, callback_pos) #to read [x y vx wz] values
        pos_client()
    except rospy.ROSInterruptException:
        rospy.loginfo("Failed in execution: program interrupted before completion", file=sys.stderr)
