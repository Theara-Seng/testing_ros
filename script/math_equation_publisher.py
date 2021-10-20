#!/usr/bin/env python


import rospy 
from testing_ros.msg import array_math   #import the message library of the float64 array

x=[1,1000,1,1000]

class math_array:
        #global x 
     
        def __init__(self):
                
                self.addition=0
                self.subtraction=0
                self.multiplication=0
                self.division=0
                
                rospy.init_node("math_array_publisher")
                self.array_pub=rospy.Publisher("math_equation",array_math,queue_size=10)
                
                
        def math_publisher(self):
                equ=array_math()
                equ.array_math=x
                self.array_pub.publish(equ)

        def math_add(self):
                x[0]+=1

        def math_sub(self):
                x[1]-=1
                
        def math_mul(self):
                x[2]=x[2]*1
        
        def math_div(self):
                x[3]=x[3]/1
                
if __name__=="__main__":
        
        equation=math_array()
        rate=rospy.Rate(10)
        
        while not rospy.is_shutdown():
                equation.math_publisher()
                equation.math_add()
                equation.math_sub()
                equation.math_mul()
                equation.math_div()
                rate.sleep()
                
        rospy.spin()
