


import _emlobjectframe as LO
import _el1objectframe as O

def el1c(lo):
    tlo = type(lo)
    if tlo is LO.Literal:
        return O.Literal(el1c(lo.obj))
    elif tlo is LO.Sign:
        return O.Sign(lo.sis)
    elif tlo is LO.String:
        return O.String(lo.sts)
    elif tlo is LO.Int:
        return O.Int(lo.n)
    elif tlo is LO.Bool:
        return O.Bool(lo.b)
    
    elif tlo is LO.Tuple:
        return O.Tuple(el1c(a) for a in lo.tl)
    elif tlo is LO.List:
        return O.List(el1c(a) for a in lo.ll)
    elif tlo is LO.Huple:
        return O.Huple(el1c(lo.hthead), [el1c(a) for a in lo.htl])
    elif tlo is LO.Hist:
        return O.Hist(el1c(lo.hlhead), [el1c(a) for a in lo.hll])
    elif tlo is LO.Call:
        return O.Call(el1c(lo.cthead), [el1c(a) for a in lo.ctl])
    elif tlo is LO.Cali:
        return O.Cali(el1c(lo.clhead), [el1c(a) for a in lo.cll])
    
    assert 0
        

__all__ = ["el1c"]
