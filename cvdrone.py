#!/usr/bin/env python
#edited by $umanth
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped

rospy.init_node('drone', anonymous=True)

mid = PoseStamped()

def callback(data):
    global mid
    mid=data
    assign(data)

rospy.Subscriber("cv_bounding_box", PoseStamped, callback)

current_pos = PoseStamped()

def current_pos_callback(position):

    global current_pos
    current_pos = position

rospy.Subscriber('mavros/local_position/pose',PoseStamped,current_pos_callback)

def assign(data):
    print("x: ")
    print(data.pose.position.x-320)
    print("y: ")
    print(data.pose.position.y-240)


    mid.pose.position.x=data.pose.position.x-320
    mid.pose.position.y=data.pose.position.y-240
    setvel_client = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel',TwistStamped, queue_size=1)
    velocity_msg = TwistStamped()

    velocity_msg.twist.linear.x = (mid.pose.position.x)*0.02
    velocity_msg.twist.linear.y = -(mid.pose.position.y)*0.02 
    if (mid.pose.position.x < 75) and (mid.pose.position.y < 75):
	velocity_msg.twist.linear.z = -1 

    setvel_client.publish(velocity_msg)

rospy.spin()
