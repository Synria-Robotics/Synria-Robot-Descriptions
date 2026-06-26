import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

# Module-level urdf attribute for when variant is None or empty string
urdf = os.path.join(_MODULE_PATH, "Corina_v1_2.urdf")

Corina_v1_2 = SimpleNamespace()
Corina_v1_2.urdf = os.path.join(_MODULE_PATH, "Corina_v1_2.urdf")
