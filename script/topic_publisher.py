#!/usr/bin/env python

import rospy

from std_msgs.msg import Int64

rospy.init_node("topic_publisher")

pub=rospy.Publisher("counter",Int64,queue_size=10)

rate=rospy.Rate(2)


count=0

while not rospy.is_shutdown():
        
        pub.publish(count)
        count+=1
        rate.sleep()
        
