"""
.. module:: coordinates_srv
    
	    :platform: Unix
	    :synopsis: Python module for the coordinates_srv service
	    :author: Marmolino Giorgio


This node is a service node, implementing a request/response communication. It uses the `SentCoords` service 
(defined in the `/srv` folder with `SentCoords.srv`). Specifically, this service implements only the response part, 
which returns two values related to the last target position coordinates sent by the user. 
There is no client that sends a request.

The response part of the `.srv` file consists of a string message and two `float32` values. To call the service, 
you can use the following command:

.. code-block:: bash

    rosservice call /SentCoord

It will return the following:

.. code-block:: text

    - Info: "Last target sent coordinates: "
    - Pos_x_sent: [value]
    - Pos_y_sent: [value]
    
"""



#! /usr/bin/env python
import rospy
import assignment2_1_rt.msg
from geometry_msgs.msg import PoseStamped
from assignment2_1_rt.srv import SentCoords, SentCoordsResponse

trg_x = 0.0
trg_y = 0.0
info = "Last target sent coordinates: "
    


def see_values(req):  # For service
    """
    
    This function retrieves the target coordinates from the ROS parameter server using the `rospy.get_param` function, 
    and stores these values in two global variables that represent the target (x, y) coordinates.
    
    :param req: The request object (not used in this case, as it is a response-only service).
    :returns: A `SentCoordsResponse` object containing the string and the target coordinates.
    
    """
    global trg_x, trg_y, info
    trg_x = rospy.get_param('target_x')
    trg_y = rospy.get_param('target_y')
    
    return SentCoordsResponse(info, trg_x, trg_y)


def get_coords():  # Main function

    """
    
    
    This function initializes the ROS node, sets up the `SentCoord` service, and starts the service loop with `rospy.spin`.
    
    :returns: None
    
    """
    rospy.init_node('coordinates_service')
    rospy.Service('SentCoord', SentCoords, see_values) 
    rospy.spin()


if __name__ == "__main__":
    get_coords()

