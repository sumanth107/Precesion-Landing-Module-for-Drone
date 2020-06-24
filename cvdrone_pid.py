#!/usr/bin/env python
#@uthor :  $umanth_Nethi
import rospy
import numpy as np
import PID
import time
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped

rospy.init_node('drone', anonymous=True)
global P, I, D, pid_x, pid_y 

P = 0.004
I = 0.000005
D = 0.0005
pid_x = PID.PID(P, I, D)
pid_x.SetPoint = 0.0
pid_x.setSampleTime(0.01)
pid_y = PID.PID(P, I, D)
pid_y.SetPoint = 0.0
pid_y.setSampleTime(0.01)

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
    pid_x.update(del_X)
    output_x = pid_x.output
    pid_y.update(del_Y)
    output_y = pid_y.output
    time.sleep(0.001)

    print("Delta_X: "),
    print(del_X)
    print("Delta_Y: "),
    print(del_Y)
    print('Pixel Dist: '),
    print(s)    
    print('PID Outputs :'),
    print(output_x, output_y)
    print('------------------------------')
    

    setvel_client = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel',TwistStamped, queue_size=1)
    velocity_msg = TwistStamped()

    velocity_msg.twist.linear.x = -output_x
    velocity_msg.twist.linear.y = -output_y
    if s < 200:
	velocity_msg.twist.linear.z = -1

    setvel_client.publish(velocity_msg)

rospy.spin()
