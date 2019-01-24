
# use command "python el1e.py <inputname1> <inputname2>" to work
# 原本，应当返回一个对象。但是传统命令行下没法接收对象，故不显示结果。

from _el1e_f import el1e   # errorlanguage1 explainer

from sys import argv
from pickle import load

assert __name__ == "__main__"

if len(argv) < 3:
    print('use command "python el1e.py <inputname1> <inputname2>" to work')
else:
    with open(argv[1],'rb') as fileobj:
        epr = load(fileobj)
    with open(argv[2],'rb') as fileobj:
        evr = load(fileobj)
    el1e(epr,evr)   # 没法以某个方式返回
        
    
