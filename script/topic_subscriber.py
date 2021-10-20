#!/usr/bin/env python

import rospy
from testing_ros.msg import robot_data
from std_msgs.msg import Int8

x=0
robot_datas=robot_data()
def callback_counter(msg):
        x=msg.data
        print('counter=%0.2f'%msg.data)
        
        

rospy.init_node("topic_subscriber")
pub1=rospy.Publisher("speeds",robot_data,queue_size=10)
sub=rospy.Subscriber("counter",Int8,callback_counter)

rate=rospy.Rate(2)



while not rospy.is_shutdown():
        robot_datas.mean_speed=x/10
        pub1.publish(robot_datas)
        #robot_data.speed+=1
        rospy.spin()
        rate.sleep()
        



