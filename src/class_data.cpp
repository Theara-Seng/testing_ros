#include<ros/ros.h>
#include<testing_ros/robot_data.h>
#include<sstream>

class data_publish{

public:
	data_publish();
	void loop();
	void publish_data();
	void speed_data();
private:
	ros::NodeHandle nh;
	ros::Publisher datas_pub;
	ros::Publisher speed_pub;
	
	
	
};
int main(int argc , char **argv){
		
		ros::init(argc,argv,"class_data");
		
		try {
			
			data_publish data_publish;
			data_publish.publish_data();
			//data_publish.speed_data();
			data_publish.loop();
			
		}
		catch(int e){
			
			if (e==0){
				return -1;
			}
		}
	
	return 0;
}
data_publish::data_publish(){
        datas_pub=nh.advertise<testing_ros::robot_data>("class_pub",10);
        speed_pub=nh.advertise<testing_ros::robot_data>("speed_pub",10);

}
void data_publish::publish_data(){
        testing_ros::robot_data datas;
        ros::Rate loop_rate(1);
        datas.speed=2;
        datas.position=1;
        datas.acceleration=1;
        testing_ros::robot_data datass;
        datass.speed=2;
        datass.position=2;
        datass.acceleration=1;
        while (ros::ok())       {
        datas_pub.publish(datas);
         speed_pub.publish(datass);
        loop_rate.sleep();
            
        }
}

        

void data_publish::loop(){
        ros::spinOnce();
}
