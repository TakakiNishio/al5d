#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(10) # 10Hz
    hello_str = JointState()
    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['joint1', 'joint2', 'joint3', 'joint4']
    hello_str.position = [3, 0.5418, -1.7297, -3.1017]
    hello_str.velocity = [0.1, 0.1, 0.1, 0.1]
    hello_str.effort = []

    while not rospy.is_shutdown():
        hello_str.header.stamp = rospy.Time.now()
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
