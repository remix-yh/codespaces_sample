import launch
from launch_ros.actions import Node

def generate_launch_description():
    return launch.LaunchDescription([
        Node(
            package='py_debug_practice',
            executable='listener',
            name='listener_node'
        ),
        Node(
            package='py_debug_practice',
            executable='talker',
            name='taker_node'
        ),
    ])
