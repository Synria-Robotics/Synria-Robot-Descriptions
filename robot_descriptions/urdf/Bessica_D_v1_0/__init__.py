import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

Bessica_D_v1_0_Covered = SimpleNamespace()
Bessica_D_v1_0_Covered.urdf = os.path.join(_MODULE_PATH, "Bessica_D_v1_0_Covered.urdf")

Bessica_D_v1_0_Skeleton = SimpleNamespace()
Bessica_D_v1_0_Skeleton.urdf = os.path.join(_MODULE_PATH, "Bessica_D_v1_0_Skeleton.urdf")