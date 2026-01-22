import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))



Bessica_D_v1_1_covered = SimpleNamespace()
Bessica_D_v1_1_covered.urdf = os.path.join(_MODULE_PATH, "Bessica_D_v1_1_covered.urdf")