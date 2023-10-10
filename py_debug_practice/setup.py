from setuptools import find_packages, setup
import os
import glob

package_name = 'py_debug_practice'

launch_files = [f for f in glob.glob('launch/**', recursive=True) if not os.path.isdir(f)]

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', launch_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='remix',
    maintainer_email='remix.re.yh@gmail.com',
    description='py_debug_practice',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_debug_practice.publisher_member_function:main',
            'listener = py_debug_practice.subscriber_member_function:main',
        ],
    },
)
