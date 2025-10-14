# Synria 机器人描述文件

[English](README_EN.md) | 中文

本仓库包含 Synria 机器人平台的 URDF（统一机器人描述格式）和 MJCF（MuJoCo 建模格式）模型。

## 仓库结构

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

## 产品

### Alicia-D v5.4
- **位置**: `urdf/Alicia-D_v5_4/` 和 `mjcf/Alicia-D_v5_4/`
- **描述**: 灵动操作臂
- **URDF**: [`alicia_d_with_gripper.urdf`](urdf/Alicia-D_v5_4/alicia_d_with_gripper.urdf)
- **MuJoCo XML**: [`alicia_d_with_gripper.xml`](mjcf/Alicia-D_v5_4/alicia_d_with_gripper.xml)

**特性:**
- 6自由度机械臂
- 集成夹爪系统
- 工具中心点 (TCP) 定义
- 支持 MuJoCo 物理仿真

### Alicia-D v5.5
- **位置**: `urdf/Alicia-D_v5_5/` 和 `mjcf/Alicia-D_v5_5/`
- **描述**: 灵动操作臂

#### 50mm 夹爪配置
- **URDF**: [`alicia_d_gripper_50mm.urdf`](urdf/Alicia-D_v5_5/alicia_d_gripper_50mm.urdf)
- **MuJoCo XML**: [`alicia_d_gripper_50mm.xml`](mjcf/Alicia-D_v5_5/alicia_d_gripper_50mm.xml)

#### 100mm 夹爪配置
- **URDF**: [`alicia_d_gripper_100mm.urdf`](urdf/Alicia-D_v5_5/alicia_d_gripper_100mm.urdf)
- **MuJoCo XML**: [`alicia_d_gripper_100mm.xml`](mjcf/Alicia-D_v5_5/alicia_d_gripper_100mm.xml)

### Bessica-D v1.0
- **位置**: `urdf/Bessica-D_v1_0/` 和 `mjcf/Bessica-D_v1_0/`
- **描述**: 灵越双臂机器人

#### 无外壳版
- **URDF**: [`bessica_D_skeleton.urdf`](urdf/Bessica-D_v1_0/bessica_D_skeleton.urdf)
- **MuJoCo XML**: [`Bessica-D_Interactive.xml`](mjcf/Bessica-D_v1_0/Bessica-D_Interactive.xml)

#### 带外壳版
- **URDF**: [`Bessica-D_Covered.urdf`](urdf/Bessica-D_v1_0/Bessica-D_Covered.urdf)
- **MuJoCo XML**: [`Bessica-D_Covered.xml`](mjcf/Bessica-D_v1_0/Bessica-D_Covered.xml)

**特性:**
- 双 7 自由度机械臂

## 使用说明

1. **URDF 文件**: 用于 ROS 集成和机器人控制
2. **MJCF 文件**: 用于 MuJoCo 物理仿真

## 支持的仿真环境

- ROS/ROS2 (通过 URDF)
- MuJoCo (通过 MJCF)
- Gazebo (通过 URDF)
- PyBullet (通过 URDF)
- Isaac Sim (通过 URDF)


