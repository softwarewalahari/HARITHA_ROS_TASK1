from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
import os
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'world', default_value='empty.world', description='Gazebo world to load'),

        # Start gzserver with the necessary plugins
        Node(
            package='gazebo_ros',
            executable='gzserver',
            name='gazebo',
            output='screen',
            parameters=[{'world_name': LaunchConfiguration('world')}],
            extra_arguments=[('--plugin', 'libgazebo_ros_factory.so')]  # This loads the GazeboRosFactory plugin
        ),

        # Start gzclient
        Node(
            package='gazebo_ros',
            executable='gzclient',
            name='gzclient',
            output='screen'
        ),
    ])
