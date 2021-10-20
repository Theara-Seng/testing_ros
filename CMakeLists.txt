cmake_minimum_required(VERSION 3.0.2)
project(testing_ros)


find_package(catkin REQUIRED COMPONENTS
  std_msgs
  roscpp
  rospy
  tf
  message_generation
  
)


 add_message_files(
   FILES
   robot_data.msg
   times.msg
   maths.msg
   array_math.msg
  # Message2.msg
 )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs  # Or other packages containing msgs

   
 )


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES testing_ros
# CATKIN_DEPENDS message_generation roscpp rospy tf
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
 add_executable(data_subscriber src/data_subscriber.cpp)
 target_link_libraries(data_subscriber ${catkin_LIBRARIES} )
  add_executable(data_publisher src/data_publisher.cpp)
 target_link_libraries(data_publisher ${catkin_LIBRARIES} )
   add_executable(class_data src/class_data.cpp)
 target_link_libraries(class_data ${catkin_LIBRARIES} )
    add_executable(class_data_subscriber src/class_data_subscriber.cpp)
 target_link_libraries(class_data_subscriber ${catkin_LIBRARIES} )

