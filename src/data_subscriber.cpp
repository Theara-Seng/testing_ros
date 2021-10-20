#include<ros/ros.h>
#include<testing_ros/robot_data.h>
#include<sstream>

int x,y,z;
void robot_data_callback(const testing_ros::robot_data::ConstPtr &robot_data){
       x=robot_data->speed;
       y=robot_data->position;
       z=robot_data->acceleration;
       
       ROS_INFO("x=%0.2f y=%.2f z=%.2f", robot_data->speed, robot_data->position,robot_data->acceleration);

}

int main(int argc,char **argv){

        ros::init(argc,argv,"robot_subscriber");
        ros::NodeHandle nh;
        
        ros::Subscriber sub=nh.subscribe("robot_data",10,robot_data_callback);
        ros::Rate loop_rate(10);
        while(ros::ok()){
        
        
                ros::spinOnce();
                loop_rate.sleep();
        }
        return 0;
        



}
