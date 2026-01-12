# SynriaRD: Synria Robotics 玄雅科技 | 机器人标准模型文件

[English](README.md) | 中文

本仓库包含 Synria Robotics 玄雅科技机器人平台的 URDF 和 MJCF 模型。

## 仓库结构

```
├── synriard
│   ├── meshes
│   │   ├── Alicia_D_v5_5
│   │   ├── Alicia_D_v5_6
│   │   ├── Alicia_M_v1_0
│   │   ├── Alicia_M_v1_1
│   │   ├── Bessica_D_v1_0
│   │   ├── Bessica_D_v1_1
│   │   └── Bessica_M_v1_0
│   ├── mjcf
│   │   ├── Alicia_D_v5_5
│   │   ├── Alicia_D_v5_6
│   │   ├── Alicia_M_v1_1
│   │   ├── Bessica_D_v1_0
│   │   ├── Bessica_D_v1_1
│   │   └── Bessica_M_v1_0
│   └── urdf
│       ├── Alicia_D_v5_5
│       ├── Alicia_D_v5_6
│       ├── Alicia_M_v1_0
│       ├── Alicia_M_v1_1
│       ├── Bessica_D_v1_0
│       ├── Bessica_D_v1_1
│       └── Bessica_M_v1_0
```

## 命名规范

所有模型文件遵循统一的命名格式：`{name}_{version}_{variant}.{ext}`

- **name**: 机器人名称（如 `Alicia_D`, `Alicia_M`, `Bessica_D`, `Bessica_M`）
- **version**: 版本号（如 `v5_5`, `v5_6`, `v1_0`, `v1_1`）
- **variant**: 其他标识
  - 对于带夹爪的机器人（Alicia_D, Alicia_M）：`gripper_{size}`（如 `gripper_50mm`, `gripper_100mm`）
  - 其他：（如 `covered`, `skeleton`, `skeleton_interactive`）
- **ext**: 文件扩展名（`.urdf` 或 `.xml`）


### 使用 API

```python
from synriard import get_model_path, list_available_models

# 获取模型路径
urdf_path = get_model_path("Alicia_D", version="v5_6", variant="gripper_50mm")
mjcf_path = get_model_path("Alicia_D", version="v5_6", variant="gripper_50mm", model_format="mjcf")

# 列出所有可用模型
print(list_available_models(model_format="urdf"))
print(list_available_models(model_format="urdf", show_path=True))
```

## 产品

### Alicia-D 
- **描述**: 灵动操作臂
- **自由度**： 6
- **夹爪配置**：50mm 和 100mm
- **版本**：v5.5, v5.6
- **变体**：
  - `gripper_50mm` - 50mm 夹爪
  - `gripper_100mm` - 100mm 夹爪
  - `leader` - 示教臂（仅 v5.6）
  - `vertical_50mm` - 垂直 50mm （仅 v5.6）
- **位置**：
  - [`Alicia_D_v5_5`](synriard/urdf/Alicia_D_v5_5)
  - [`Alicia_D_v5_6`](synriard/urdf/Alicia_D_v5_6)

### Alicia-M 
- **描述**: 云擎操作臂
- **自由度**： 6
- **版本**：v1.0, v1.1
- **夹爪配置**：100mm
- **位置**：
  - [`Alicia_M_v1_0`](synriard/urdf/Alicia_M_v1_0)
  - [`Alicia_M_v1_1`](synriard/urdf/Alicia_M_v1_1)

### Bessica-D 
- **描述**: 灵越双臂人形机器人
- **自由度**：14 （双 7 自由度机械臂）
- **版本**：v1.0, v1.1
- **外观**：无外壳版和外壳版

#### 无外壳版
- **v1.0 URDF**: [`Bessica_D_v1_0_skeleton.urdf`](synriard/urdf/Bessica_D_v1_0/Bessica_D_v1_0_skeleton.urdf)
- **v1.0 MuJoCo XML**: [`Bessica_D_v1_0_skeleton.xml`](synriard/mjcf/Bessica_D_v1_0/Bessica_D_v1_0_skeleton.xml)
- **v1.1 URDF**: [`Bessica_D_v1_1_skeleton.urdf`](synriard/urdf/Bessica_D_v1_1/Bessica_D_v1_1_skeleton.urdf)
- **v1.1 MuJoCo XML**: [`Bessica_D_v1_1_skeleton.xml`](synriard/mjcf/Bessica_D_v1_1/Bessica_D_v1_1_skeleton.xml)
- **v1.1 MuJoCo XML (交互式)**: [`Bessica_D_v1_1_skeleton_interactive.xml`](synriard/mjcf/Bessica_D_v1_1/Bessica_D_v1_1_skeleton_interactive.xml)

#### 带外壳版（仅 v1.0）
- **URDF**: [`Bessica_D_v1_0_covered.urdf`](synriard/urdf/Bessica_D_v1_0/Bessica_D_v1_0_covered.urdf)
- **MuJoCo XML**: [`Bessica_D_v1_0_covered.xml`](synriard/mjcf/Bessica_D_v1_0/Bessica_D_v1_0_covered.xml)
- **MuJoCo XML (交互式)**: [`Bessica_D_v1_0_covered_interactive.xml`](synriard/mjcf/Bessica_D_v1_0/Bessica_D_v1_0_covered_interactive.xml)

### Bessica-M 
- **描述**: 灵越双臂人形机器人（M 系列）
- **自由度**：14 （双 7 自由度机械臂）
- **版本**：v1.0
- **位置**：[`Bessica_M_v1_0`](synriard/urdf/Bessica_M_v1_0)

## 添加新机器人模型

添加新机器人模型后，运行自动化脚本自动生成所需的 `__init__.py` 文件：

```bash
# 1. 添加模型文件到对应目录
mkdir -p synriard/mjcf/RobotName_v1_0
cp RobotName_v1_0_gripper_100mm.xml synriard/mjcf/RobotName_v1_0/

# 2. 运行自动化脚本
python3 auto_generate_init.py

# 脚本会自动：
# - 生成每个机器人目录的 __init__.py
# - 更新父目录的 __init__.py 注册所有机器人
```

脚本选项：
- `--format mjcf|urdf|all`: 指定处理的格式（默认：all）
- `--synriard-path PATH`: 指定 synriard 目录路径（默认：自动检测）

## 支持的仿真环境

- ROS/ROS2 
- MuJoCo 
- Gazebo 
- PyBullet
- IsaacSim / IsaacLab
