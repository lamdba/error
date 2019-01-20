
# use command "python lc.py <inputname> <outputname>" to work

from _require import lc

from sys import argv
# ~ from dill import dump

assert __name__ == "__main__"

if len(argv) < 3:
    print('use command "python lc.py <inputname> <outputname>" to work')
else:
    with open(argv[1],'r') as fileobj:
        s = fileobj.read()
    obj = lc(s)     # lc 报错方式值得分析……虽说不重要，又是“ERROR or RESULT”问题
    with open(argv[2],'wb') as fileobj:
        # dump(obj,fileobj) # it's error
        # so, you can't save this thing easy. you need your 序列化方法 即使 这或许是不大可能的
        
    