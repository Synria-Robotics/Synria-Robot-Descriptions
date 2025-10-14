# Synria Robot Descriptions

English | [中文](README.md)

This repository contains URDF (Unified Robot Description Format) and MJCF (MuJoCo Modeling Format) models for Synria robotic platforms.

## Repository Structure

```
├── meshes
│   ├── Alicia-D_v5_4
│   ├── Alicia-D_v5_5
│   └── Bessica-D_v1_0
├── mjcf
│   ├── Alicia-D_v5_4
│   ├── Alicia-D_v5_5
│   └── Bessica-D_v1_0
└── urdf
    ├── Alicia-D_v5_4
    ├── Alicia-D_v5_5
    └── Bessica-D_v1_0
```

## Robot Platforms

### Alicia-D v5.4
- **Location**: `urdf/Alicia-D_v5_4/` and `mjcf/Alicia-D_v5_4/`
- **Description**: Agile manipulation arm
- **URDF**: [`alicia_d_with_gripper.urdf`](urdf/Alicia-D_v5_4/alicia_d_with_gripper.urdf)
- **MuJoCo XML**: [`alicia_d_with_gripper.xml`](mjcf/Alicia-D_v5_4/alicia_d_with_gripper.xml)

**Features:**
- 6-DOF robotic arm
- MuJoCo physics simulation support

### Alicia-D v5.5
- **Location**: `urdf/Alicia-D_v5_5/` and `mjcf/Alicia-D_v5_5/`
- **Description**: Agile manipulation arm (multiple gripper configurations)

#### 50mm Gripper Configuration
- **URDF**: [`alicia_d_gripper_50mm.urdf`](urdf/Alicia-D_v5_5/alicia_d_gripper_50mm.urdf)
- **MuJoCo XML**: [`alicia_d_gripper_50mm.xml`](mjcf/Alicia-D_v5_5/alicia_d_gripper_50mm.xml)

#### 100mm Gripper Configuration
- **URDF**: [`alicia_d_gripper_100mm.urdf`](urdf/Alicia-D_v5_5/alicia_d_gripper_100mm.urdf)
- **MuJoCo XML**: [`alicia_d_gripper_100mm.xml`](mjcf/Alicia-D_v5_5/alicia_d_gripper_100mm.xml)

### Bessica-D v1.0
- **Location**: `urdf/Bessica-D_v1_0/` and `mjcf/Bessica-D_v1_0/`
- **Description**: Dual-arm robotic platform

#### Skeleton Version
- **URDF**: [`bessica_D_skeleton.urdf`](urdf/Bessica-D_v1_0/bessica_D_skeleton.urdf)
- **MuJoCo XML**: [`Bessica-D_Interactive.xml`](mjcf/Bessica-D_v1_0/Bessica-D_Interactive.xml)

#### Covered Version
- **URDF**: [`Bessica-D_Covered.urdf`](urdf/Bessica-D_v1_0/Bessica-D_Covered.urdf)
- **MuJoCo XML**: [`Bessica-D_Covered.xml`](mjcf/Bessica-D_v1_0/Bessica-D_Covered.xml)

**Features:**
- Dual 7-DOF manipulator arms

## Usage

1. **URDF Files**: For ROS integration and robot control
2. **MJCF Files**: For MuJoCo physics simulation

## Supported Simulation Environments

- ROS/ROS2 (via URDF)
- MuJoCo (via MJCF)
- Gazebo (via URDF)
- PyBullet (via URDF)
- Issac Sim (via URDF)