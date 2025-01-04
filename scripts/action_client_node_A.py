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



OdPose = Pose()
OdTwist = Twist()
pub_PsVl = rospy.Publisher("/posVel", PosVel, queue_size = 10)
msg_PsVl = PosVel()# message to be published

'''
NODE DESCRIPTION:

The client waits for the user to enter a valid target position for the robot given by [x y] coordinates;
once the goal is sent, the user is allowed to cancel the sent goal pressing 'k' in the terminal command line;
if the user doesn't cancel the goal sent, the system will work without interruptions until the target position
is reached; once the target position is reached, the node will display a message confirming the goal.
'''

def pos_client(): #this works as the main function

    rospy.init_node('bug_action_client')
    rospy.Subscriber("/odom", Odometry, odom_callback)#to read odometry values
    
    pub_target = rospy.Publisher("/targetPosition", PoseStamped, queue_size=10)
    act_pos = PoseStamped()

    #as standard from launch file parameters:
    act_pos.pose.position.x = rospy.get_param('target_x')
    act_pos.pose.position.y = rospy.get_param('target_y')
    act_pos.pose.position.z = 0.0


    client = actionlib.SimpleActionClient('/reaching_goal', assignment2_1_rt.msg.PlanningAction)
    client.wait_for_server()
    
    

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

        #we can change the target position
        rospy.loginfo("\n enter goal position as [x y] values: ")
        act_pos.pose.position.x = float(input("X value: "))
        act_pos.pose.position.y = float(input("Y value: "))
        act_pos.pose.position.z = 0.0
        goal = assignment2_1_rt.msg.PlanningGoal(target_pose=act_pos)
        client.send_goal(goal)

        cancel = input("Press 'k' to cancel the sent target coordinates: ")
        while(client.get_state() != actionlib.GoalStatus.SUCCEEDED):
            #pub_target.publish(act_pos) #publish on topic value
            if cancel == 'k':
                    client.cancel_goal()
                    rospy.loginfo("Goal deletion: confirmed")
                    break
        
        if(client.get_state() == actionlib.GoalStatus.SUCCEEDED):
            rospy.loginfo("Robot has been reached the target position")

        pos_callback()
        rate.sleep()


        
def pos_callback():
        global pub_PsVl #publisher
        global OdPose   #pose from odometry
        global OdTwist  #twist from odometry

        PsVl = PosVel() #define a PosVel var to be used to send the custom message
        PsVl.pos_x = OdPose.position.x
        PsVl.pos_y = OdPose.position.y
        PsVl.vel_x = OdTwist.linear.x
        PsVl.vel_z = OdTwist.angular.z
        pub_PsVl.publish(PsVl) #publish on a custom message

def odom_callback(msg_PsVl):
    global OdPose
    global OdTwist
    OdPose = msg_PsVl.pose.pose
    OdTwist = msg_PsVl.twist.twist

if __name__ == '__main__':
    pos_client()
