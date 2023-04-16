#!/usr/bin/env python
import os
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose
from my_turtlebot_localization.srv import MyServiceMessage, MyServiceMessageResponse

# MyServiceMessage:

# # request
# string label
# ---
# #response
# bool navigation_successfull
# string message

# rosmsg info geometry_msgs/PoseWithCovarianceStamped:

# std_msgs/Header header
#   uint32 seq
#   time stamp
#   string frame_id
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

# rosmsg info geometry_msgs/Pose:

# geometry_msgs/Point position
#   float64 x
#   float64 y
#   float64 z
# geometry_msgs/Quaternion orientation
#   float64 x
#   float64 y
#   float64 z
#   float64 w


class spot_storage_class():

    def __init__(self):

        # define the '/amcl_pose' subscriber
        self.amcl_pose_sub = rospy.Subscriber(
            '/amcl_pose', PoseWithCovarianceStamped, self.sub_callback)
        # for receive the subscription
        self.pose_with_cov = PoseWithCovarianceStamped()
        # for record 'pose' for service
        self.pose = Pose()

        # define service server for spots recording
        self.spot_recorder_service_server = rospy.Service(
            '/save_spot', MyServiceMessage, self.service_callback)

        # file path
        self.spots_dir = '/home/user/catkin_ws/src/my_turtlebot_localization/spots'
        # indicator for the fact whether the message is saved correctly, defaultly false
        self.indicator = False

    def sub_callback(self, msg):

        # only record the 'pose' information from '/amcl_pose'
        self.pose.position = msg.pose.pose.position
        self.pose.orientation = msg.pose.pose.orientation

    def service_callback(self, request):

        self.label = request.label
        spot_recorder_response = MyServiceMessageResponse()

        if self.label == 'end':

            rospy.loginfo("the service ends")
            spot_recorder_response.navigation_successfull = True
            spot_recorder_response.message = 'the recording is done'

        else:

            spot_recorder_response.navigation_successfull = True
            files_lst = os.listdir(self.spots_dir)
            for file in files_lst:
                if file.endswith('.txt'):
                    # the txt-file containing messages is found
                    # self.indicator = True
                    file_path = self.spots_dir + '/' + file
                    # keep the content which are already in the txt-file
                    with open(file_path, 'a') as spot_rec:
                        spot_rec.write('\n' + self.label + ':')
                        spot_rec.write('\n' + str(self.pose) + '\n')
                    rospy.loginfo("current label is: " + str(self.label))
                    rospy.loginfo("current pose is: " + str(self.pose))
                    spot_recorder_response.message = f'position {self.label[6:]} is recorded'

        # if self.indicator == True:
        #     spot_recorder_response.message = 'the recording is done'

        return spot_recorder_response

    def main(self):

        rospy.loginfo("the service is ready......")
        rospy.loginfo("call the service for spots recording with: ")
        rospy.loginfo("rosservice call /save_spot \"label corner1\" ")
        rospy.loginfo("or")
        rospy.loginfo("rosservice call /save_spot \"end\" ")
        rospy.spin()


if __name__ == '__main__':
    rospy.init_node('spot_recorder')
    SpotStore = spot_storage_class()
    SpotStore.main()
