
"""
内置环境
"""
from _el1objectframe import * 
from _el1e_core import updated  
from _evr_base import evr_base
from _lc_f import lc
from _el1c_f import el1c
from _el1e_f import el1e

"evr = lib + base"

with open("_stdlib.el1") as fileobj:
    libcode = fileobj.read()

lib = el1e(el1c(lc(libcode)),evr_base)
evr_std = Namespace(updated(evr_base.d,lib.d))  # 其实应该在基操作中找updated

__all__ = ["evr_std"]

