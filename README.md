# Mobile Robot with Four Wheels
# Overview

This project involves creating a four-wheeled mobile robot and simulating it in the Gazebo environment using ROS 2. The robot's URDF and simulation are configured within the mobile_robot_description package in the ROS 2 workspace.

# Workspace Structure
ros2_humble_ws/
├── src/
│   └── mobile_robot_description/
│       ├── launch/
│       │   ├── spawn_robot.launch.py
│       │   ├── gazebo.launch.py
│       │   └── display.launch.py
│       └── urdf/
│           └── mobile_base_generated.urdf

# Launch Files:

    spawn_robot.launch.py: Spawns the robot in Gazebo.

    gazebo.launch.py: Starts the Gazebo simulation with the robot.

    display.launch.py: Launches the robot's visualization.

# URDF:

    The robot's URDF (mobile_base_generated.urdf) is used to describe its physical properties, joints, and sensors.

Steps to Run the Simulation
irst, source the ROS 2 workspace:

  # 1.  Source ROS 2 Workspace source 
  ros2_humble_ws/install/setup.bash

  # 2. Start Gazebo
    Launch the Gazebo simulation using the following command: ros2 launch mobile_robot_description gazebo.launch.py

  # 3.Spawn the Robot in Gazebo
After launching Gazebo, you can spawn the robot using the spawn robot launch file: ros2 launch mobile_robot_description spawn_robot.launch.py

 # 4.Visualize the Robot (Optional):If you'd like to visualize the robot in Rviz, run the display launch file: ros2 launch mobile_robot_description display.launch.py

# Dependencies

Ensure that the following dependencies are installed in your workspace:

    ROS 2 Humble

    Gazebo

    ROS 2 packages for Gazebo (gazebo_ros)

# Conclusion

This setup simulates a basic four-wheeled mobile robot and provides an interface for controlling and visualizing it within the ROS 2 ecosystem and Gazebo.
