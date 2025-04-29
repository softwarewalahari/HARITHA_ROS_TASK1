from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_gazebo_ros = FindPackageShare('gazebo_ros')
    pkg_mobile_robot = FindPackageShare('mobile_robot_description')

    urdf_path = PathJoinSubstitution([
        pkg_mobile_robot,
        'urdf',
        'mobile_base_generated.urdf'  # Make sure this filename is correct
    ])

    return LaunchDescription([
        # Launch Gazebo with empty world
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    pkg_gazebo_ros,
                    'launch',
                    'gazebo.launch.py'
                ])
            )
        ),

        # Publish robot description to /robot_description
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': urdf_path}]
        ),

        # Spawn robot into Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            arguments=['-topic', 'robot_description', '-entity', 'mobile_base'],
            output='screen'
        )
    ])
