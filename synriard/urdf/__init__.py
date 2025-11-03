# This line makes the sub-folders available as attributes of this module
from . import Alicia_D_v5_5
from . import Alicia_D_v5_6
from . import Bessica_D_v1_0

# 注意：不要在此处导入具体的 URDF 命名空间对象（例如 Bessica_D_v1_0_Covered），
# 否则在某些环境下会触发“partially initialized module”循环导入错误。
# 正确用法：通过子包访问，如
#   from robot_descriptions import urdf
#   urdf_path = urdf.Bessica_D_v1_0.Bessica_D_v1_0_Covered.urdf

__all__ = [
    "Alicia_D_v5_5",
    "Alicia_D_v5_6",
    "Bessica_D_v1_0",
]
