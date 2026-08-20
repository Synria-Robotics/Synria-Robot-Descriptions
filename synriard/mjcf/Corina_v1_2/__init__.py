import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

Corina_v1_2 = SimpleNamespace()
Corina_v1_2.xml = os.path.join(_MODULE_PATH, "Corina_v1_2.xml")
