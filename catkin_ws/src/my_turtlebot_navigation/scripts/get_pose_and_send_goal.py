#! /usr/bin/env python
import rospy
import actionlib
import os
from my_turtlebot_localization.srv import MyServiceMessage, MyServiceMessageResponse
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult
from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from math import sqrt

# MyServiceMessage:

# # request
# string label
# ---
# #response
# bool navigation_successfull
# string message

# rostopic info /imu:

# Type: sensor_msgs/Imu
# Publishers:
#  * /gazebo (http://3_xterm:38617/)
# Subscribers: None

# rosmsg info sensor_msgs/Imu:

# std_msgs/Header header
#   uint32 seq
#   time stamp
#   string frame_id
# geometry_msgs/Quaternion orientation
#   float64 x
#   float64 y
#   float64 z
#   float64 w
# float64[9] orientation_covariance
# geometry_msgs/Vector3 angular_velocity
#   float64 x
#   float64 y
#   float64 z
# float64[9] angular_velocity_covariance
# geometry_msgs/Vector3 linear_acceleration
#   float64 x
#   float64 y
#   float64 z
# float64[9] linear_acceleration_covariance

# rostopic info /odom:

# Type: nav_msgs/Odometry
# Publishers:
#  * /gazebo (http://3_xterm:38617/)
# Subscribers:
#  * /move_base (http://3_xterm:43215/)

# rosmsg info nav_msgs/Odometry:

# std_msgs/Header header
#   uint32 seq
#   time stamp
#   string frame_id
# string child_frame_id
# geometry_msgs/PoseWithCovariance pose
#   geometry_msgs/Pose pose
#     geometry_msgs/Point position
#       float64 x
#       float64 y
#       float64 z
#     geometry_msgs/Quaternion orientation
#       float64 x
#       float64 y
#       float64 z
#       float64 w
#   float64[36] covariance
# geometry_msgs/TwistWithCovariance twist
#   geometry_msgs/Twist twist
#     geometry_msgs/Vector3 linear
#       float64 x
#       float64 y
#       float64 z
#     geometry_msgs/Vector3 angular
#       float64 x
#       float64 y
#       float64 z
#   float64[36] covariance


class get_pose_and_send_goal_class():

    def __init__(self):

        # define service server to get poses from spots.txt
        self.get_pose_service_server = rospy.Service(
            '/get_pose_service', MyServiceMessage, self.service_callback)

        # define action client to call '/move_base' to send goals
        # which were received from service '/get_pose_service'
        self.send_goal_action_client = actionlib.SimpleActionClient(
            '/move_base', MoveBaseAction)
        rospy.loginfo('waiting for action client for sending goals......')
        self.send_goal_action_client.wait_for_server()
        rospy.loginfo('the client is ready......')
        self.goal = MoveBaseGoal()

        # define subscriber of topic '/odom' to determine current pose
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.sub_callback)
        self.current_pose = Odometry()

        # other information
        self.spots_txt = '/home/user/catkin_ws/src/my_turtlebot_localization/spots/spots.txt'

    def get_difference(self):

        pos_x = self.current_pose.pose.pose.position.x
        pos_y = self.current_pose.pose.pose.position.y
        ori_z = self.current_pose.pose.pose.orientation.z
        ori_w = self.current_pose.pose.pose.orientation.w

        goal_pos_x = self.goal.target_pose.pose.position.x
        goal_pos_y = self.goal.target_pose.pose.position.y
        goal_ori_z = self.goal.target_pose.pose.orientation.z
        goal_ori_w = self.current_pose.pose.pose.orientation.w

        difference = sqrt((goal_pos_x-pos_x)**2 + (goal_pos_y-pos_y) **
                          2 + (goal_ori_z-ori_z)**2 + (goal_ori_w-ori_w)**2)
        rospy.loginfo(
            'the difference between goal and current pose is: ' + str(difference))
        rospy.loginfo('current pose: pos_x={}, pos_y={},ori_z={},ori_w={}'.format(
            pos_x, pos_y, ori_z, ori_w))
        rospy.loginfo('goal pose: pos_x={}, pos_y={},ori_z={},ori_w={}'.format(
            goal_pos_x, goal_pos_y, goal_ori_z, goal_ori_w))

        return difference

    def sub_callback(self, msg):

        self.current_pose = msg

    def feedback_callback(self, feedback):

        rospy.loginfo('robot is going to the pose......')

    def service_callback(self, request):

        self.service_response = MyServiceMessageResponse()

        # due to the situation that the pose and only 4 necessary values:
        # position.x, position.y, orientation.z, orientation.w
        # others are all equal to 0
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.z = 0
        self.goal.target_pose.pose.orientation.x = 0
        self.goal.target_pose.pose.orientation.y = 0

        # get labels in spots.txt
        self.desired_label = request.label
        spots_file = open(self.spots_txt, 'r')
        # to count how many values are already extracted
        count = 0
        # indicator of whether the desired label is found
        find_it = False
        for idx, line in enumerate(spots_file):
            # check if the label is desired
            if line[6:-2] == self.desired_label:
                find_it = True
                continue
            # check if all 4 values are insert into dict
            if count >= 4:
                break
            # if the desired label is found, insert values into dict
            if find_it == True:
                if (idx+1) % 11 == 3:
                    value = line.strip().split(':')
                    self.goal.target_pose.pose.position.x = float(value[1])
                    count += 1
                elif (idx+1) % 11 == 4:
                    value = line.strip().split(':')
                    self.goal.target_pose.pose.position.y = float(value[1])
                    count += 1
                elif (idx+1) % 11 == 9:
                    value = line.strip().split(':')
                    self.goal.target_pose.pose.orientation.z = float(value[1])
                    count += 1
                elif (idx+1) % 11 == 10:
                    value = line.strip().split(':')
                    self.goal.target_pose.pose.orientation.w = float(value[1])
                    count += 1
        spots_file.close()

        print('the goal is: ')
        print(self.goal)

        # send goals to '/move_base'
        self.send_goal_action_client.send_goal(
            self.goal, feedback_cb=self.feedback_callback)

        self.send_goal_action_client.wait_for_result()
        rospy.loginfo('the result is: ' +
                      str(self.send_goal_action_client.get_state()))

        # check if the navigation is successful
        difference = self.get_difference()
        tolerance = 5
        if difference < tolerance:

            self.service_response.message = 'OK'
            self.service_response.navigation_successfull = True

        return self.service_response

    def main(self):

        rospy.loginfo("the service is ready......")
        rospy.loginfo("call the service for getting pose with: ")
        rospy.loginfo("rosservice call /get_pose_service \"corner1\" ")
        rospy.spin()


if __name__ == '__main__':

    rospy.init_node('get_pose_and_send_goal_node')
    GetPoseAndSendGoal = get_pose_and_send_goal_class()
    GetPoseAndSendGoal.main()
