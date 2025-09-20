# Synria Robot Descriptions

English | [中文](README.md)

This repository contains URDF (Unified Robot Description Format) models for Synria robotic platforms.

## Repository Structure

```
.
├── README.md
├── README_EN.md
├── README_CN.md
├── AliciaD/
│   └── v5_4/
│       └── gripper50mm/
│           ├── meshes/
│           └── urdf/
└── BessicaD/
    ├── BessicaDOnly/
    │   ├── meshes/
    │   └── urdf/
    └── BessicaDwithCover/
        ├── meshes/
        └── urdf/
```

## Robot Platforms

### AliciaD v5.4
- **Location**: [`AliciaD/v5_4/gripper50mm/`](AliciaD/v5_4/gripper50mm/)
- **Description**: Dual-arm robotic platform with 50mm gripper configuration
- **Main URDF**: [`alicia_duo_with_gripper.urdf`](AliciaD/v5_4/gripper50mm/urdf/alicia_duo_with_gripper.urdf)
- **MuJoCo XML**: [`alicia_duo_with_gripper.xml`](AliciaD/v5_4/gripper50mm/urdf/alicia_duo_with_gripper.xml)

**Features:**
- 7-DOF dual arms
- Integrated gripper system
- Tool center point (TCP) definition
- MuJoCo physics simulation support

### BessicaD
Two variants are available:

#### BessicaD Only
- **Location**: [`BessicaD/BessicaDOnly/`](BessicaD/BessicaDOnly/)
- **Main URDF**: [`bessica_D_v2_1.urdf`](BessicaD/BessicaDOnly/urdf/bessica_D_v2_1.urdf)
- **MuJoCo XML**: [`bessica_D_v2_1.xml`](BessicaD/BessicaDOnly/urdf/bessica_D_v2_1.xml)

#### BessicaD with Cover
- **Location**: [`BessicaD/BessicaDwithCover/`](BessicaD/BessicaDwithCover/)
- **Main URDF**: [`BessicaDCodver.urdf`](BessicaD/BessicaDwithCover/urdf/BessicaDCodver.urdf)
- **MuJoCo XML**: [`BessicaDCodver.xml`](BessicaD/BessicaDwithCover/urdf/BessicaDCodver.xml)

**Features:**
- Dual 7-DOF manipulator arms
- Prismatic gripper joints
- Base platform with mounting points
- Collision meshes and visual representations
- Inertial properties for realistic simulation
