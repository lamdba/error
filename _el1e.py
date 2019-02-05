

from _el1e_core import eval    # 对象类也引入

def el1e(epr,evr):
    return eval(epr,evr.d)

__all__ = ["el1e"]
