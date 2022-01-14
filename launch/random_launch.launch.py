from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='action_python',
            # namespace='random_client',
            name='random_server',
            executable='random_server'

        ),

        Node(
            package='action_python',
            # namespace='random_client',
            name='random_action_client',
            executable='random_client'

        )
    

    
    
    ])

