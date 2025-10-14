import os
from types import SimpleNamespace

# Get the absolute path to THIS directory
_MODULE_PATH = os.path.dirname(os.path.abspath(__file__))

# Define the paths for this specific robot version.
# NOTE: You may need to check the actual filenames inside the
# 'Alicia_D_v5_4' folder and adjust the names below.

# Example: if the demo script needed a gripper from v5.4
# alicia_d_gripper_35mm = SimpleNamespace()
# alicia_d_gripper_35mm.urdf = os.path.join(_MODULE_PATH, "alicia_d_gripper_35mm.urdf")

# Even if this version isn't used by the demo, it's good practice
# to have it not cause an import error. Leaving it empty is also fine.

alicia_d_with_gripper = SimpleNamespace()
alicia_d_with_gripper.urdf = os.path.join(_MODULE_PATH, "alicia_d_with_gripper.urdf")
