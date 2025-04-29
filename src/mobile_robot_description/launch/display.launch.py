#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
import os
import xacro

def generate_launch_description():
    # Process Xacro file
    xacro_file = os.path.join(
        os.path.dirname(__file__), "..", "urdf", "mobile_base.urdf.xacro"
    )
    robot_description_config = xacro.process_file(xacro_file)
    robot_description = {"robot_description": robot_description_config.toxml()}

    return LaunchDescription([
        # Robot State Publisher Node
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[robot_description],
        ),

        # Gazebo simulation node (spawning the robot)
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            name="spawn_entity",
            output="screen",
            arguments=[
                "-entity", "mobile_base",
                "-file", os.path.join(
                    os.path.dirname(__file__), "..", "urdf", "mobile_base.urdf.xacro"
                ),
            ],
        ),
    ])
