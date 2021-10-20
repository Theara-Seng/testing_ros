#include<ros/ros.h>
#include<testing_ros/robot_data.h>
#include<testing_ros/times.h>
#include<sstream>

class data_subscriber{

public: 
        data_subscriber();
        //void data_time(const testing_
        void loop();
      //  void subscribe_data(const testing_ros::robot_data::ConstPtr& robot_data);

private:
        ros::NodeHandle nh;
        ros::Subscriber sub;

        void data_callback(const testing_ros::robot_data::ConstPtr& robot_data);
        
};

int main(int argc, char **argv){
        
        ros::init(argc,argv,"class_data_subscriber");
        
        try {
                data_subscriber data_subscriber;
                data_subscriber.loop();
        }
        catch (int e){
        
                if (e==0){
                        return -1;
                }
        }
        
        
        return 0;

}       

data_subscriber::data_subscriber(){
        sub=nh.subscribe<testing_ros::robot_data>("speed_pub",10,&data_subscriber::data_callback,this);
}
void data_subscriber::loop(){
        ros::spin();
}
void data_subscriber::data_callback(const testing_ros::robot_data::ConstPtr& robot_data){
       
       
       ROS_INFO("speed=%0.2f position=%0.2f acceleration=%0.2f",robot_data->speed,robot_data->position,robot_data->acceleration);
}
