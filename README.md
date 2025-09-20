# Synria 机器人描述文件

[English](README_EN.md) | 中文

本仓库包含 Synria 机器人平台的 URDF（统一机器人描述格式）模型。

## 仓库结构

```
.
├── README.md
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

## 产品

### AliciaD v5.4
- **位置**: [`AliciaD/v5_4/gripper50mm/`](AliciaD/v5_4/gripper50mm/)
- **描述**: 灵动操作臂（50mm行程夹爪）


### BessicaD

#### 灵越基础版
- **位置**: [`BessicaD/BessicaDOnly/`](BessicaD/BessicaDOnly/)
- **URDF**: [`bessica_D_v2_1.urdf`](BessicaD/BessicaDOnly/urdf/bessica_D_v2_1.urdf)
- **MuJoCo XML**: [`bessica_D_v2_1.xml`](BessicaD/BessicaDOnly/urdf/bessica_D_v2_1.xml)

#### 灵越带外壳
- **位置**: [`BessicaD/BessicaDwithCover/`](BessicaD/BessicaDwithCover/)
- **URDF**: [`BessicaDCodver.urdf`](BessicaD/BessicaDwithCover/urdf/BessicaDCodver.urdf)
- **MuJoCo XML**: [`BessicaDCodver.xml`](BessicaD/BessicaDwithCover/urdf/BessicaDCodver.xml)


