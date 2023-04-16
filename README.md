# ROS Navigation Rosject

This project is a tutorial of the course **ROS Navigation in 5 Days** from [TheConstruct](https://app.theconstructsim.com/).

## Project Introduction
The basic simulation of models(including robots, contexts) and notebook content are offered by TheConstruct. Only the **catkin_ws** is created by user. This project show complete process about basic ROS navigation.

### ROS Version
* ROS Noetic on Ubuntu20

### Technologies
* rospy
* xml
* yaml

## Introduction of Packages for Navigation
There are 4 main packages provided in ROS for navigation: **gmapping** package, **map_server** package, **AMCL** package and **move_base** package.

### gmapping package

1. Launch the **gmapping** package with .launch file
2. Start a **slam_gmapping node** (from the gmapping package)
3. **slam_gmapping node** subscribes to the **Laser Topic** and the **Transform Topics (/tf)** to gets data and builds a map
4. The generated map is published during the whole process into the **/map** topic

### map_server package

#### map_saver node: save map

1. Launch the **map_saver node**
2. Access the map data from a ROS Service
3. Save map into 2 files: .pdm for image itself, map metadata and the image name for YAML file

#### map_server node: provide map

1. Read a map file from the disk
2. Provides the map to any other node that requests it via a ROS **Service**
3. **static_map (nav_msgs/GetMap)**: Provides the map occupancy data through this service.

### AMCL(Adaptive Monte Carlo Localization) package: estimate position

1. Provide the **amcl node** to track the localization of a robot moving in a 2D space
2. Subscribe to the **laser topic (/scan),** the **map topic (/map),** and the **transform topic (/tf)**
3. Publish **estimated position** to the **/amcl_pose** and the **/particlecloud** topics

### move_base package: path planning

1. Provide **move_base** node to move the robot from its current position to a goal position
2. Operate **goal pose** through **action server**
3. *SimpleActionClient* publishes to the topic */move_base/goal* to send the pose goal
4. *SimpleActionServer* subscribes to the topic */move_base/goal* to read the pose goal

#### Global planner: calculate a safe path to arrive at that goal pose

1. **move_base node** recceived a new **goal pose**
2. The **new goal pose** is sent to **global planner**
3. **global planner** calculates a **path** before robot starts to move
4. The **path** is published into **topic /plan**

#### Global Costmap

1. Created from a user-generated static map (check Mapping Chapter)
2. Used by global planner

#### Local planner: tweak local path during movement

1. **global planner** calculates a **global path**
2. The **global path** is sent to **local planner**
3. According to segments of **global path**, adjust **local path**
4. Publish **local path** into **topic** **/local_plan**
5. Publish the part of the **global plan** to be followed into the **topic** **/global_plan**
6. Provide velocity command to move robot

#### Local Costmap

1. Used by **local planner** to calculate **local plans**
2. Created directly from the robot's sensor readings
3. Keep the robot in the center of the costmap as it moves throughout the environment
4. Drop obstacle information from the map as the robot moves

## catkin_ws Description
The basic navigation functions in ROS include: map creation, localization and path planning, which are indiviaully implemented by the following packages: **my_turtlebot_mapping**, **my_turtlebot_localization**, **my_turtlebot_path_planning**. The last one package **my_turtlebot_navigation** covers all functions above and extra calling of one **service**, which will be in details later.

### my_turtlebot_mapping

1. Map creation with **slam_gmapping** node
2. Map saving with **map_saver**
3. Map providing with **map_server**

### my_turtlebot_localization

1. Localization with **amcl** node
2. Record spots into .txt file

### my_turtlebot_path_planning

1. Extract spots from .txt file as **goal**
2. Path planning with **global planner** and **local planner**

## Getting Started

1. Start **Gazebo** by:
```
roslaunch realrobotlab main.launch
```

2. Use keyboard to control turtlebot by:
```
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

3. Map creation by:
```
roslaunch my_turtlebot_mapping rosject_gmapping.launch
```
when **rviz** is launched, move robot around the environment. Make sure laser scans every corner.

4. After the map is created, in another terminal, run:
```
rosrun map_server map_saver -f name_of_map
```
This command will give .pdm and .yaml of map file.

5. Run **amcl** node to implement localization and record random pose information into **my_turtlebot_localization/spots/spots.txt** by:
```
roslaunch my_turtlebot_localization rosject_spotsrecorder_amcl.launch
```
Move robot around, and record a pose **corner1**(for example) with:
```
rosservice call /save_spot "label corner1"
```

6. Run **move_base** node with:
```
roslaunch my_turtlebot_navigation rosject_all_navigation.launch
```

7. Provide a pose for robot to move to **corner1** (for example):
```
rosservice call /get_pose_service "corner1" 
```
