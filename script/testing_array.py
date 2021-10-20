#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray

if __name__=="__main__":
        
        rospy.init_node("array_publish")
        array_pub=rospy.Publisher("Array_Publisher",Float64MultiArray,queue_size=10)
        
        rate=rospy.Rate(10)
        
        while not rospy.is_shutdown():
                test=Float64MultiArray()
                
                test.data=[1,2,3,4,5]
                array_pub.publish(test)
                
        rospy.spin()
