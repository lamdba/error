
# [quickclass] 
# fast way to make dataclasses

from functools import wraps


def createclass(name:"classname",l:"list of propertynames"):
    
    def __init__(self,*a):
        assert len(a) == len(l)
        for k,v in zip(l,a):
            setattr(self,k,v)
    return type(name,(),{"__init__":wraps(name,l)(__init__)})



def localmake(d:"local dict",name,l):
    d[name] = createclass(name,l)


__all__ = ["createclass","localmake"]
