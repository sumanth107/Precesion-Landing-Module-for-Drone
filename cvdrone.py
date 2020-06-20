#!/usr/bin/env python
#@uthor : Sumanth Nethi
import rospy
import numpy as np
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped

rospy.init_node('drone', anonymous=True)

def callback(data):
    assign(data)

rospy.Subscriber("cv_bounding_box", PoseStamped, callback)

current_pos = PoseStamped()

def current_pos_callback(position):
    global current_pos
    current_pos = position

rospy.Subscriber('mavros/local_position/pose',PoseStamped,current_pos_callback)

def assign(data):

    del_X = data.pose.position.x-320
    del_Y = 240-data.pose.position.y
    s = np.sqrt(del_X**2 + del_Y**2)

    print("Delta_X: "),
    print(del_X)
    print("Delta_Y: "),
    print(del_Y)
    print('Pixel Dist: '),
    print(s)
    print('------------------------------')
    
    setvel_client = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel',TwistStamped, queue_size=1)
    velocity_msg = TwistStamped()

    velocity_msg.twist.linear.x = del_X*0.02
    velocity_msg.twist.linear.y = del_Y*0.02 
    if s < 200:
	velocity_msg.twist.linear.z = -1

    setvel_client.publish(velocity_msg)

rospy.spin()
