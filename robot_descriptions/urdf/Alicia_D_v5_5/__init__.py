import os
from types import SimpleNamespace

# Get the absolute path to THIS directory (__init__.py's location)
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

Alicia_D_gripper_50mm = SimpleNamespace()
Alicia_D_gripper_100mm = SimpleNamespace()

Alicia_D_gripper_50mm.urdf = os.path.join(_MODULE_PATH, "Alicia_D_gripper_50mm.urdf")

Alicia_D_gripper_100mm.urdf = os.path.join(_MODULE_PATH, "Alicia_D_gripper_100mm.urdf")