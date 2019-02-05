
"""
内置环境
"""
from _el1objectframe import Namespace
from _el1e_core import updated  
from _baseevr import baseevr
from _lc import lc
from _el1c import el1c
from _el1e import el1e

"stdevr = lib + base"

with open("_stdlib.el1") as fileobj:
    libcode = fileobj.read()

lib = el1e(el1c(lc(libcode)),baseevr)
stdevr = Namespace(updated(baseevr.d,lib.d))  # 其实应该在基操作中找updated

__all__ = ["stdevr"]

