#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Function to find all data files
def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

# Collect all mesh, URDF, and MJCF files
extra_files = []
extra_files += package_files('meshes')
extra_files += package_files('urdf')
extra_files += package_files('mjcf')

setup(
    name="synria_robot_descriptions",
    version="1.0.0",
    author="Synria Robotics",
    author_email="support@synriarobotics.ai",
    description="URDF and MJCF robot description files for Synria robotic platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/synria-robotics/synria-robot-descriptions",
    project_urls={
        "Bug Tracker": "https://github.com/synria-robotics/synria-robot-descriptions/issues",
        "Documentation": "https://github.com/synria-robotics/synria-robot-descriptions",
        "Source Code": "https://github.com/synria-robotics/synria-robot-descriptions",
    },
    packages=find_packages(),
    package_data={
        '': extra_files,
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No Python dependencies required for robot description files
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
        "ros": [
            # ROS-related dependencies if needed
        ],
    },
    keywords="robotics, urdf, mjcf, robot-description, simulation, mujoco, ros",
    entry_points={
        "console_scripts": [
            # Add any command-line tools if needed in the future
        ],
    },
    zip_safe=False,  # Required for package data files
)