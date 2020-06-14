#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
rospy.init_node('opencv_example', anonymous=True)

def show_image(img):
  cv2.namedWindow("Image Window")
  cv2.imshow("Image Window", img)
  cv2.waitKey(3)


def image_callback(img_msg):
  rospy.loginfo(img_msg.header)
  cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
  show_image(cv_image)   

sub_image = rospy.Subscriber("/webcam/image_raw", Image, image_callback)

rospy.spin()
