#!/usr/bin/env python

import math as m

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def deg2rad(deg):

    rad = []
    rad.append(float(deg[0]*(m.pi/180)))
    rad.append(float(deg[1]*(m.pi/180)))
    rad.append(float(deg[2]*(m.pi/180)))
    rad.append(float(deg[3]*(m.pi/180)))

    return rad


def talker(theta):
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10) # 10Hz
    al5d_str = JointState()
    al5d_str.header = Header()
    al5d_str.header.stamp = rospy.Time.now()
    al5d_str.name = ['joint1', 'joint2', 'joint3', 'joint4']
    al5d_str.position = theta
    al5d_str.velocity = []
    al5d_str.effort = []

    while not rospy.is_shutdown():
        al5d_str.header.stamp = rospy.Time.now()
        pub.publish(al5d_str)
        rate.sleep()

if __name__ == '__main__':

    theta_deg = []

    print "imput each joint angle in deg."
    print "theta_base:"
    theta_deg.append(float(raw_input('>>>  ')))
    print "theta_shoulder:"
    theta_deg.append(float(raw_input('>>>  ')))
    print "theta_elbow:"
    theta_deg.append(float(raw_input('>>>  ')))
    print "theta_wrist:"
    theta_deg.append(float(raw_input('>>>  ')))

    theta_rad = deg2rad(theta_deg)

    talker(theta_rad)
