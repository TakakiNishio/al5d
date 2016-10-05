#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

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
        hello_str.header.stamp = rospy.Time.now()
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    talker()
