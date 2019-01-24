
"""
内置环境
"""
from _el1e_core import *    # 对象类也引入


def make_name(l,evr):   # 最好还要重整命名……t和l，输入为e
    for a in l.ll:
        if type(a) is not Sign:exit("Name should be sign")
    return A(l.ll)


def make_namespace(a,evr):
    d = dict()
    for pair in a.ll:
        pair = eval(pair,evr)
        t = pair.tl
        k, v = t
        if type(k) is not Sign:exit("Namespace's key must be sign")
        d[k.sis] = eval(v,evr)
    return Namespace(d)


def retmethod(a,evr):
    name,a = a.tl  # name在前
    a = eval(a,evr)
    if type(name) is not Sign: exit("Error: method must be sign")
    return getmethod(a,name.sis)


def make_object(a,evr):
    d1,d2 = a.tl
    d1 = eval(d1,evr)
    d2 = eval(d2,evr)
    return Object(d1.d,d2.d)



def make_function(a,evr):
    arglname, e = a.tl        # e 不求值，所以这里必须是字面表达式
    # Sign Expression
    return Function(arglname.sis,e,{})

def quote(a,evr):
    a, = a.tl
    return a

def let(a,evr):
    namespace, e = a.tl
    namespace = eval(namespace,evr)
    # Namespace Expression
    return eval(e,updated(evr,namespace.d))     # 是比上级多这些

def unpack(a,evr):
    t1, t2 = a.tl


    t1 = eval(t1,evr)
    t2 = eval(t2,evr)
    return Namespace(dict(zip((a.sis for a in t1.l), t2.tl)))

def now(a,evr):
    d, = a.tl
    d = eval(d,evr)
    return Namespace({k:eval(v,evr) for k,v in d.d.items()})

def _if(a,evr):
    b,e1,e2 = a.tl
    b = eval(b,evr)
    if b.b:     # phuck!
        return eval(e1,evr)
    else:
        return eval(e2,evr)

def _print(a,evr):
    a, = a.tl
    a = eval(a,evr)
    print(apply(getmethod(a,"str"),Tuple([]),evr).sts)
    return a

evr_base_d = {
"Names":Baseoperating(make_name),
"Namespace":Baseoperating(make_namespace),
"Function":Baseoperating(make_function),
"Object":Baseoperating(make_object),

"'":Baseoperating(quote),

"unpack":Baseoperating(unpack),

"if":Baseoperating(_if),
"print":Baseoperating(_print),


"getmethod":Baseoperating(retmethod),

"let":Baseoperating(let),      # 其实用unpack前的东西（ns不透明不行）可以写出let，通过临时构造一个函数
"now":Baseoperating(now),      # 用now是不对的，应该依次求值
}

evr_base = Namespace(evr_base_d)

__all__ = ["evr_base"]
