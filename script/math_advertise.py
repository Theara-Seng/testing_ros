#!/usr/bin/env python

import rospy
from testing_ros.msg import maths

class math_advertise:

        def __init__(self,add_value,sub_value,mul_value,div_value):
        
        
                self.add_value=add_value
                self.sub_value=sub_value
                self.mul_value=mul_value
                self.div_value=div_value
                
               
                self.add_pub = rospy.Publisher("add_value",maths,queue_size=5)
                self.sub_pub = rospy.Publisher("sub_value",maths,queue_size=5)
                self.mul_pub = rospy.Publisher("mul_value",maths,queue_size=5)
                self.div_pub = rospy.Publisher("div_value",maths,queue_size=5)
                self.mean_pub = rospy.Publisher("mean_value",maths,queue_size=5)
                self.var_pub = rospy.Publisher("variance_value",maths,queue_size=5)
                
        def add_values(self):
                
                self.add_value+=self.add_value
                
        def sub_values(self):
        
                self.sub_value-=1
                
        def add_publish(self):
        
                add=maths()
                add.add=self.add_value
               
                self.add_pub.publish(add)
                print(add)
                
        def sub_publish(self):
                sub=maths()
                sub.sub=self.sub_value
                self.sub_pub.publish(sub)
                print(sub)

        def mul_publish(self):
                mul=maths()
                mul.mul=self.mul_value
                self.mul_pub.publish(mul)
                print(mul)
       
        def mul_values(self):
                self.mul_value*=2
        

        
if __name__=='__main__':
        rospy.init_node("math_advertise")
        math =math_advertise(1.0,1.0,2.0,1.0)
        rate=rospy.Rate(0.1)
        while not rospy.is_shutdown():
                
                math.sub_publish()
                math.sub_values()
                
                math.add_publish()
                math.add_values()
                
                math.mul_publish()
                math.mul_values()
                
                rate.sleep()
        rospy.spin() 
        
