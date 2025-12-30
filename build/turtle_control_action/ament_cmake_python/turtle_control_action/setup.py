from setuptools import find_packages
from setuptools import setup

setup(
    name='turtle_control_action',
    version='0.0.0',
    packages=find_packages(
        include=('turtle_control_action', 'turtle_control_action.*')),
)
