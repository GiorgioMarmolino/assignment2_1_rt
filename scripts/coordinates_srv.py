#! /usr/bin/env python
import rospy 
import assignment2_1_rt.msg
from geometry_msgs.msg import PoseStamped
from assignment2_1_rt.srv import SentCoords, SentCoordsResponse

trg_x = 0.0
trg_y = 0.0

def get_target_sent(see_trg): #for subscriber
    global trg_x
    global trg_y
    trg_x = see_trg.pose.position.x
    trg_y = see_trg.pose.position.y

    
def see_values(req): #fro service
    global trg_x
    global trg_y
     #rospy.loginfo("Target sent has coordinates:\n X: %f \n Y: %f" %(trg_x, trg_y))
     return SentCoordsResponse(trg_x, trg_y)

def get_coords(): #main function
    rospy.init_node('coordinates_service')
    rospy.Subscriber('/targetPosition', PoseStamped, get_target_sent)
    rospy.Service('SentCoord', SentCoords, see_values) 
    rospy.spin()

if __name__ == "__main__":
        get_coords()