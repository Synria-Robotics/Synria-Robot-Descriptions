import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

Alicia_M_v1_1_bi_vertical_interactive = SimpleNamespace()
Alicia_M_v1_1_bi_vertical_interactive.xml = os.path.join(_MODULE_PATH, "Alicia_M_v1_1_bi_vertical_interactive.xml")

Alicia_M_v1_1_follower = SimpleNamespace()
Alicia_M_v1_1_follower.xml = os.path.join(_MODULE_PATH, "Alicia_M_v1_1_follower.xml")

Alicia_M_v1_1_follower_interactive = SimpleNamespace()
Alicia_M_v1_1_follower_interactive.xml = os.path.join(_MODULE_PATH, "Alicia_M_v1_1_follower_interactive.xml")

Alicia_M_v1_1_vertical = SimpleNamespace()
Alicia_M_v1_1_vertical.xml = os.path.join(_MODULE_PATH, "Alicia_M_v1_1_vertical.xml")
