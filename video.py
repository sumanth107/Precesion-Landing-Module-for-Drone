#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()
rospy.init_node('opencv_example', anonymous=True)

def show_image(img):
  cv2.namedWindow("Image Window")
  im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  cv2.imshow("Image Window", im_rgb)
  cv2.waitKey(3)


def image_callback(img_msg):
  rospy.loginfo(img_msg.header)
  cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
  show_image(cv_image)   

sub_image = rospy.Subscriber("/webcam/image_raw", Image, image_callback)

rospy.spin()
