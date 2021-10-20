#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool
from testing_ros.msg import robot_data

class NumberCounter:

    def __init__(self):
        self.counter = 0
        self.timer=0
        self.pub = rospy.Publisher("/number_count", Int64, queue_size=10)
        self.pubs= rospy.Publisher("/timer_pub",robot_data,queue_size=10)
        self.number_subscriber = rospy.Subscriber("/number", Int64, self.callback_number)
        self.time_subscriber =rospy.Subscriber("speed_pub",robot_data,self.callback_timer)
        self.reset_service = rospy.Service("/reset_counter", SetBool, self.callback_reset_counter)

    def callback_number(self, msg):
        self.counter += msg.data
        new_msg = Int64()
        new_msg.data = self.counter
        self.pub.publish(new_msg)
        
    def callback_timer(self, da):
        self.timer +=da.speed
        datass=robot_data()
        datass.speed=self.timer
        self.pubs.publish(datass);
        print("speed=",da.speed)

    def callback_reset_counter(self, req):
        if req.data:
            self.counter = 0
            return True, "Counter has been successfully reset"
        return False, "Counter has not been reset"
   
 
 


if __name__ == '__main__':
    rospy.init_node('number_counter')
    
    NumberCounter()
    rospy.spin()
