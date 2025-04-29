from setuptools import setup
import os
from glob import glob

package_name = 'mobile_robot_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    data_files=[
        (os.path.join('share', package_name), ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf.xacro')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='haritha',
    maintainer_email='haritha@todo.todo',
    description='Mobile robot with base and wheels',
    license='MIT',
    tests_require=['pytest'],
    entry_points={},
)
