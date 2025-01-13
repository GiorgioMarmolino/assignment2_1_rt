#! /usr/bin/env python
import rospy 
import assignment2_1_rt.msg
from assignment2_1_rt.srv import Stop, StopResponse
from assignment2_1_rt.msg import PlanningAction

info = "Robot has been stopped"
 
def stop_robot(req): #for service
    global info
    client = actionlib.SimpleActionClient('/reaching_goal', assignment2_1_rt.msg.PlanningAction)
    client.wait_for_server()
    client.cancel_goal()
    return StopResponse(info)

if __name__ == "__main__":
    rospy.init_node('stop_service')
    rospy.Service('Stop', Stop, stop_robot) 
    rospy.spin()


    
    


