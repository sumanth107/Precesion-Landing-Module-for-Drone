#!/usr/bin/env python

#@uthor : Sumanth_Nethi

import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import PoseStamped

midpoint = PoseStamped()
#lower1 = np.array([0, 120, 70])    #limits for red object detection
#upper1 = np.array([10, 255, 255])
lower = np.array([110, 50, 50])     # blue limits
upper = np.array([130, 255, 255])
#lower2 = np.array([170, 120, 70])  
#upper2 = np.array([180, 255, 255])

bridge = CvBridge()
rospy.init_node('opencv_1', anonymous=True)
publisher=rospy.Publisher('cv_bounding_box', PoseStamped,queue_size=20)

def show_image(img):
  cv2.namedWindow("Image Window")
  frame_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

  #mask1 = cv2.inRange(frame_HSV, lower1, upper1)
  #mask2 = cv2.inRange(frame_HSV, lower2, upper2)
  #mask = mask1 + mask2
  mask = cv2.inRange(frame_HSV, lower, upper)
  mask_Open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((10, 10)))
  mask_Close = cv2.morphologyEx(mask_Open, cv2.MORPH_CLOSE, np.ones((20, 20))) 
  mask_Perfect = mask_Close
  conts, h = cv2.findContours(mask_Perfect.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  
  areas = [cv2.contourArea(c) for c in conts] 
  if areas != []:
  	max_index = np.argmax(areas)
  	cnt=conts[max_index]
  	x, y, w, h = cv2.boundingRect(cnt)
  	cv2.rectangle(img_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)
  	cv2.circle(img_rgb, (x + int(w*0.5), y + int(h*0.5)), 4, (0,255,0), -1)   
  	midpoint.pose.position.x=x + int(w * 0.5)
  	midpoint.pose.position.y=y + int(h * 0.5)
  	midpoint.pose.position.z=0
  publisher.publish(midpoint)
  cv2.imshow("Image Window", img_rgb)
  cv2.waitKey(3)


def image_callback(img_msg):
  rospy.loginfo(img_msg.header)
  cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
  show_image(cv_image)   

sub_image = rospy.Subscriber("/webcam/image_raw", Image, image_callback)

rospy.spin()

