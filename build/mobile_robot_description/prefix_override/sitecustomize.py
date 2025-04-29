import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/haritha/ros2_humble_ws/install/mobile_robot_description'
