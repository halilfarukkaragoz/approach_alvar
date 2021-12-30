#!/usr/bin/env python

import rospy
import time
from tf.msg import tfMessage
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2


def detect_ar_tag(data):


    transform = data.transforms
    for i in transform:
        name = i.child_frame_id
        if "ar_marker_" in name:
            marker_x = i.transform.rotation.x
            marker_y = i.transform.rotation.y
            marker_z = i.transform.rotation.z
            marker_w = i.transform.rotation.w
            roll,pitch,yaw = euler_from_quaternion((marker_x ,marker_y,marker_z,marker_w))
            print( name + " " +  str(pitch))

def odom(data):

   
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z

    x_angular = data.pose.pose.orientation.x
    y_angular = data.pose.pose.orientation.y
    z_angular = data.pose.pose.orientation.z
    w_angular = data.pose.pose.orientation.w

    roll, pitch, yaw = euler_from_quaternion(
        (x_angular, y_angular, z_angular, w_angular))

if __name__ == "__main__":
    
    rospy.init_node("temp")
    rospy.Subscriber("/tf", tfMessage, detect_ar_tag)
    rospy.Subscriber("/odometry/filtered", Odometry, odom)

    rospy.spin()
    
    
