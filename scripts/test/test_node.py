#!/usr/bin/env python
import rospy
import cv2

if __name__ == '__main__':
    rospy.init_node('my_first_python_node')

    rospy.loginfo("This node has been started")

    rospy.sleep(1)

    rospy.loginfo("Exit now")