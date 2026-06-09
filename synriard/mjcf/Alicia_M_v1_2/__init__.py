import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

Alicia_M_v1_2_follower = SimpleNamespace()
Alicia_M_v1_2_follower.xml = os.path.join(_MODULE_PATH, "Alicia_M_v1_2_follower.xml")

Alicia_M_v1_2_follower_ARX = SimpleNamespace()
Alicia_M_v1_2_follower_ARX.xml = os.path.join(_MODULE_PATH, "Alicia_M_1_2_follower_ARX.xml")
