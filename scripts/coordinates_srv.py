#! /usr/bin/env python
import rospy 
import assignment2_1_rt.msg
from geometry_msgs.msg import PoseStamped
from assignment2_1_rt.srv import SentCoords, SentCoordsResponse

trg_x = 0.0
trg_y = 0.0
    
def see_values(req): #for service
    global trg_x, trg_y
    trg_x = rospy.get_param('target_x')
    trg_y = rospy.get_param('target_y')
    return SentCoordsResponse(trg_x, trg_y)

def get_coords(): #main function
    rospy.init_node('coordinates_service')
    rospy.Service('SentCoord', SentCoords, see_values) 
    rospy.spin()

if __name__ == "__main__":
    get_coords()
