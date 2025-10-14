import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

Bessica_D_Covered = SimpleNamespace()
Bessica_D_Covered.urdf = os.path.join(_MODULE_PATH, "Bessica_D_Covered.urdf")

Bessica_D_Skeleton = SimpleNamespace()
Bessica_D_Skeleton.urdf = os.path.join(_MODULE_PATH, "Bessica_D_Skeleton.urdf")