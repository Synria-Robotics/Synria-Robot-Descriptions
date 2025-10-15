import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

Bessica_D_Covered = SimpleNamespace()
Bessica_D_Covered.xml = os.path.join(_MODULE_PATH, "Bessica_D_Covered.xml")
Bessica_D_Interactive = SimpleNamespace()
Bessica_D_Interactive.xml = os.path.join(_MODULE_PATH, "Bessica_D_Interactive.xml")