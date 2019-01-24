from _evr_std import evr_std    # 对象类也引入
from pickle import dump

with open("stdevr.ns",'wb') as fileobj:
    dump(evr_std,fileobj)
