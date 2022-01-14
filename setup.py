from setuptools import setup
import os
from glob import glob

package_name = 'action_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='wjsrudwls96@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'action_client_ex = action_python.action_client_ex:main',
            'action_server_ex = action_python.action_server_ex:main',
            'random_client = action_python.random_client:main ',
            'random_server = action_python.random_server:main',

        ],
    },
)
