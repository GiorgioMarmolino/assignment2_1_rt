#! /usr/bin/env python
import rospy
import assignment2_1_rt.msg
from geometry_msgs.msg import PoseStamped
from assignment2_1_rt.srv import SentCoords, SentCoordsResponse

trg_x = 0.0
trg_y = 0.0
info = "Last target sent coordinates: "
    
"""

This node is a service node, so it means that it implements a communication of type request/response; this node use the SentCoords service 
(inside the folder */srv* we can find *SentCoords.srv*); in detail this service is composed only by the response part since it is required to return 
two values related to the last target position coordinates sent by the user, and there isn't any client that makes a request. The *.srv* response 
part is composed of a message (so a string) and two *float32* values; for calling the service it is sufficient to use the command:

.. code-block:: bash
	    
    	rosservice call /SentCoord

and it will return:

.. code-block:: text

	   - Info:	"Last target sent coordinates: "
	   - Pos_x_sent: [value]
	   - Pos_y_sent: [value]
	   
"""
def see_values(req): #for service
    """

    This function retrieves values from the list of parameters using the **rospy.get_param** function, and then it load these values in two
    global variables dedicated to the (x,y) coordinate target values.
    
    """
    global trg_x, trg_y, info
    trg_x = rospy.get_param('target_x')
    trg_y = rospy.get_param('target_y')
    
    return SentCoordsResponse(info, trg_x, trg_y)

def get_coords(): #main function
    """
    
    .. module:: coordinate_srv
    
    :platform: Unix
    :synopsis: Python module for the coordinate_srv
    
    .. moduleauthor:: Marmolino Giorgio
    
    This is the main function of the service node, it is used to initialize the service node, implement the service and spin it.
    
    """
    rospy.init_node('coordinates_service')
    rospy.Service('SentCoord', SentCoords, see_values) 
    rospy.spin()

if __name__ == "__main__":
    get_coords()
