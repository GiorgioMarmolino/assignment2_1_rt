#This .py script is related to the service node, used to return the target values (x,y) sent by the user 

import rospy 
import assignment2_1_rt.msg
from assignment2_1_rt.srv import SentCoords, SentCoordsResponse

trg_x = 0
trg_y = 0

def see_values(req):
    global trg_x
    global trg_y
    trg_x=rospy.get_param('target_x')
    trg_y=rospy.get_param('target_y')
    return SentCoordsResponse(trg_x, trg_y)

def get_coords(): #main function
    rospy.init_node('SentCoordSrv')
    s = rospy.Service('SentCoord', SentCoords, see_values) 
    rospy.spin()

if name ==" main ":
    try:
        get_coords()
    except:
        rospy.logerr("Error in node execution")