#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import Twist

noise_multiplier = 1.01

def callback(data):
    
    new_vel = data
    new_vel.angular.z = new_vel.angular.z * noise_multiplier
    pub.publish(new_vel)

if __name__ == '__main__':
    rospy.init_node('vel_noise', anonymous=True)

    rospy.Subscriber("/cmd_vel", Twist, callback)
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)

    rospy.spin()


