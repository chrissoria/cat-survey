"""Back-compat alias for `catsurvey`.

The canonical import name is `catsurvey`. `cat_survey` is retained so existing
code continues to work; prefer `catsurvey` in new code.
"""
import importlib
import sys

_canonical = "catsurvey"
_real = importlib.import_module(_canonical)

sys.modules[__name__] = _real

_src_prefix = _canonical + "."
_dst_prefix = __name__ + "."
for _name in list(sys.modules):
    if _name.startswith(_src_prefix):
        sys.modules[_dst_prefix + _name[len(_src_prefix):]] = sys.modules[_name]
