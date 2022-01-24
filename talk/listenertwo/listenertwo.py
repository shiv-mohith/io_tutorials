#!/usr/bin/env python

import rospy
import os
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + ' I heard the %s', data.data)


def listener():
	topicname=os.getenv('topic_name','telemetry2')
	rospy.init_node('listenertwo', anonymous=True)
	rospy.Subscriber(topicname, String, callback)

	rospy.spin()

if __name__ == '__main__':
	listener()
