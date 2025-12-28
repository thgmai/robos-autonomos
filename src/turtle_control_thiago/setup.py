from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtle_control_thiago'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thiago',
    maintainer_email='thiago.mai@edu.ufes.br',
    description='Pacote de controle para turtlesim',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'turtle_control = turtle_control_thiago.turtle_control:main',
            'goal_publisher = turtle_control_thiago.goal_publisher:main',
        ],
    },
)
