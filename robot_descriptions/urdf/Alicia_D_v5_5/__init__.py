import os
from types import SimpleNamespace

# Get the absolute path to THIS directory (__init__.py's location)
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

alicia_d_gripper_50mm = SimpleNamespace()

alicia_d_gripper_50mm.urdf = os.path.join(_MODULE_PATH, "alicia_d_gripper_50mm.urdf")