import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

# Define paths for the Bessica robot if needed
# bessica_d_default = SimpleNamespace()
# bessica_d_default.urdf = os.path.join(_MODULE_PATH, "bessica_d.urdf")