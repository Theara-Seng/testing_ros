#!/usr/bin/env python


import rospy 

from testing_ros.msg import array_math
from std_msgs.msg import Float64
class array_math_subscriber:
        def __init__(self):
                rospy.init_node("array_math_subscriber")
                self.sum=0.0
                self.mean=0.0
                self.variance=0.0
                self.array_sub=rospy.Subscriber("math_array",array_math,self.array_callback)
                self.mean_pub=rospy.Publisher("mean_publisher",Float64,queue_size=10)
                self.variance_pub=rospy.Publisher("variance_publisher",Float64,queue_size=10)
                
        def array_callback(self):
                arr_math=array_math()
                self.sum+=arr_math[0]
                self.mean=self.sum/len(self.sum)
                self.variance=self.mean**2
                mean=Float64()
                variance=Float64()
                mean.data=self.mean
                variance.data=self.variance
                self.mean_pub.publish(mean)
                self.variance_pub.publish(variance)

if __name__=="__main__":
        arr_sub=array_math_subscriber()
        rate=rospy.Rate(10)
        while not rospy.is_shutdown():
                rate.sleep()
                
        rospy.spin()
        
