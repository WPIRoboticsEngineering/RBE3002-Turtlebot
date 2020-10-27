#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import Twist

# Offset is measured by how many meters the robot will drift 
# per meter of distance traveled (estimate)
offset = 0.1 # meters per meter

def callback(data):
    
    new_vel = data
    # Formula below estimates the curve, uses chord length instead of arc length to simplify equation
    # This should be ok, as it is only an estimate
    new_vel.angular.z = new_vel.angular.z + new_vel.linear.x * 2 * offset
    pub.publish(new_vel)

if __name__ == '__main__':
    rospy.init_node('vel_noise', anonymous=True)

    offset = rospy.get_param("offset")

    rospy.Subscriber("cmd_vel", Twist, callback)
    pub = rospy.Publisher("cmd_vel_robot", Twist, queue_size=1)

    rospy.spin()


