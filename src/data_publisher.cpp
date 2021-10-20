#include"ros/ros.h"
#include"testing_ros/robot_data.h"
#include"sstream"

int main(int argc, char **argv){
        ros::init(argc,argv,"robot_publisher");
        ros::NodeHandle nh;
        ros::Publisher robot=nh.advertise<testing_ros::robot_data>("robot_data",1000);
        ros::Rate loop_rate(10);
        
        
        testing_ros::robot_data robot_data;
        robot_data.speed=0.0;
        robot_data.position=0.0;
        robot_data.acceleration=0.0;
        while(ros::ok()){
                robot.publish(robot_data);
                robot_data.speed+=1;
                robot_data.position=robot_data.speed/10;
                robot_data.acceleration=robot_data.speed*0.6;
                
                ROS_INFO("speed=%0.2f position=%0.2f acceleration=%0.2f",robot_data.speed,robot_data.position,robot_data.acceleration);
                
                ros::spinOnce();
                loop_rate.sleep();
                
        
        }
        return 0;


}

