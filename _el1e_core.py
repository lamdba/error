
# [el1e]
# error language 1 explainer (expression obj -> END)

from _el1objectframe import *

def updated(d,new_d):   #tool
    _ = d.copy()
    _.update(new_d)
    return _

def getname(namespace,name):
    return namespace.d[name]

def method_closure(mt,selfspace):   # 或许这东西不该叫method，而应该叫临时获得环境的函数……（相当于内置了let开头的函数）
    return Function(mt.arglname,mt.e,updated(mt.inevr,{mt.selfname:selfspace}))


def getmethod(a,name):      # 17个内部类（不包括迭代/生成器）
    if type(a) is Blackbox:
        obj = a
        return closure(obj.d_method[name],obj.d_field)

    elif type(a) is Int:      # 这里都没有检查输入类型
        if name == "succ":  # 先独有方法后普适方法
            return Function([],[],Int(a.n+1),{})
        elif name == "pred":
            return Function([],[],Int(a.n-1),{})
        elif name == "divmod":
            return Baseoperating(lambda t,evr:Tuple(list(divmod(a.n,eval(t.tl[0],evr).n))))
        elif name == "+":   # 按理还要重载正负运算
            return Baseoperating(lambda t,evr:Int(a.n+eval(t.tl[0],evr).n))
        elif name == "-":
            return Baseoperating(lambda t,evr:Int(a.n-eval(t.tl[0],evr).n))
        elif name == "*":
            return Baseoperating(lambda t,evr:Int(a.n*eval(t.tl[0],evr).n))
        elif name == "//":  # div
            return Baseoperating(lambda t,evr:Int(a.n//eval(t.tl[0],evr).n))
        elif name == "%":
            return Baseoperating(lambda t,evr:Int(a.n%eval(t.tl[0],evr).n))
        elif name == "/":   # truediv
            return Baseoperating(lambda t,evr:Float(a.n/eval(t.tl[0],evr).n))
        elif name == "^":   # 按理要重载与浮点数混用情况
            return Baseoperating(lambda t,evr:Int(a.n**eval(t.tl[0],evr).n))
        elif name == "abs":
            return Baseoperating(lambda t,evr:Int(abs(a.n)))
        elif name == "==":
            return Baseoperating(lambda t,evr:Bool(a.n == eval(t.tl[0],evr).n))
        elif name == "!=":
            return Baseoperating(lambda t,evr:Bool(a.n != eval(t.tl[0],evr).n))
        elif name == ">":
            return Baseoperating(lambda t,evr:Bool(a.n > eval(t.tl[0],evr).n))
        elif name == "<":
            return Baseoperating(lambda t,evr:Bool(a.n < eval(t.tl[0],evr).n))
        elif name == ">=":
            return Baseoperating(lambda t,evr:Bool(a.n >= eval(t.tl[0],evr).n))
        elif name == "<=":
            return Baseoperating(lambda t,evr:Bool(a.n <= eval(t.tl[0],evr).n))
        elif name == "str":
            return Baseoperating(lambda _,evr:String(str(a.n)))
    elif type(a) is Float:
        if name == "+":
            return Baseoperating(lambda t,evr:Float(a.v+eval(t.tl[0],evr).v))
        elif name == "-":
            return Baseoperating(lambda t,evr:Float(a.v-eval(t.tl[0],evr).v))
        elif name == "*":
            return Baseoperating(lambda t,evr:Float(a.v%eval(t.tl[0],evr).v))
        elif name == "/":   # truediv
            return Baseoperating(lambda t,evr:Float(a.v/eval(t.tl[0],evr).v))
        elif name == "^":
            return Baseoperating(lambda t,evr:Float(a.v**eval(t.tl[0],evr).v))
        elif name == "abs":
            return Baseoperating(lambda t,evr:Float(abs(a.v)))
        elif name == "==":
            return Baseoperating(lambda t,evr:Bool(a.v == eval(t.tl[0],evr).v))
        elif name == "!=":
            return Baseoperating(lambda t,evr:Bool(a.v != eval(t.tl[0],evr).v))
        elif name == ">":
            return Baseoperating(lambda t,evr:Bool(a.v > eval(t.tl[0],evr).v))
        elif name == "<":
            return Baseoperating(lambda t,evr:Bool(a.v < eval(t.tl[0],evr).v))
        elif name == ">=":
            return Baseoperating(lambda t,evr:Bool(a.v >= eval(t.tl[0],evr).v))
        elif name == "<=":
            return Baseoperating(lambda t,evr:Bool(a.v <= eval(t.tl[0],evr).v))
        elif name == "str":
            return Baseoperating(lambda _,evr:String(str(a.v)))
    elif type(a) is String:         # 字符串比大小没有实现
        if name == "+":
            return Baseoperating(lambda t,evr:String(a.s+eval(t.tl[0],evr).s))
        elif name == "in":
            return Baseoperating(lambda t,evr:Bool(eval(t.tl[0],evr).s in a.s))
        elif name == "==":
            return Baseoperating(lambda t,evr:Bool(a.s == eval(t.tl[0],evr).s))
        elif name == "!=":
            return Baseoperating(lambda t,evr:Bool(a.s != eval(t.tl[0],evr).s))
        elif name == "iter":
            return Baseoperating(lambda t,evr:"暂未实现迭代器")
        elif name == "len":
            return Baseoperating(lambda t,evr:Int(len(a.s)))
        elif name == "getitem":
            return Baseoperating(lambda t,evr:String(a.s[eval(t.tl[0],evr)]))   # 要不要区分字符和字符串？
        elif name == "str":
            return Baseoperating(lambda _,evr:a)
    elif type(a) is Bool:
        if name == "&":
            return Baseoperating(lambda t,evr:Bool(a.b and eval(t.tl[0],evr).b))
        elif name == "/":
            return Baseoperating(lambda t,evr:Bool(a.b or eval(t.tl[0],evr).b))
        elif name == "!":
            return Baseoperating(lambda t,evr:Bool(not a.b))
        elif name == "str":
            return Baseoperating(lambda _,evr:String(str(a.b)))

    # Tuple 无方法
    elif type(a) is List:
        if name == "getitem":
            return Baseoperating(lambda t,evr:a.l[eval(t[0],evr).n])
        if name == "len":
            return Baseoperating(lambda t,evr:Int(len(a.l)))
        if name == "iter":
            exit("now can't iter")
        if name == "+":
            return Baseoperating(lambda t,evr:List(a.l+eval(t[0],evr).l))
        if name == "append":
            return Baseoperating(lambda t,evr:List(a.l+[eval(t[0],evr)]))
        if name == "cons":
            return Baseoperating(lambda t,evr:List([eval(t[0],evr)]+a.l))
        if name == "head":
            return Baseoperating(lambda t,evr:a.l[0])
        if name == "tail":
            return Baseoperating(lambda t,evr:a.l[1:])
        if name == "init":
            return Baseoperating(lambda t,evr:a.l[:-1])
        if name == "last":
            return Baseoperating(lambda t,evr:a.l[-1])

    elif type(a) is Huple:
        if name == "head":
            return Baseoperating(lambda t,evr:a.head)
        elif name == "tail":
            return Baseoperating(lambda t,evr:Tuple(a.tail))
    elif type(a) is Hist:
        if name == "head":
            return Baseoperating(lambda t,evr:a.head)
        elif name == "tail":
            return Baseoperating(lambda t,evr:List(a.tail))

    # Namespace:  # 可以用let配符号获取其中的值
    # Names:  # 也暂不给方法
    # Function:   # 也暂不给方法，而且没有apply（但相当于表达式自己）

    # Baseoperating: #无方法


    # Call:   #无方法（有相关函数）
    # Cali:   #无方法（有相关函数）
    # Sign:   #无方法（有相关函数）
    # Literal:#无方法（有相关函数）





# 明确定义：方法是函数的闭包（不过，函数在创建时一般已经被闭包了一次）

def eval(a,evr):    # 一开始使用递归
    # ~ assert isinstance(a, ErrorBlackbox)
    if type(a) is Sign:
        return evr[a.sis]
    elif type(a) is Call:
        f = eval(a.cthead,evr)
        return apply(f,Tuple(a.ctl),evr)     # 参数部分要假装成一个字面表
    elif type(a) is Cali:
        f = eval(a.clhead,evr)
        return apply(f,List(a.cll),evr)
    elif type(a) is Literal:    # 若字面值为组合类型，那么其成员必都是字面值；并不对成员求值
        return a.obj


def apply(f,a,evr):
    # ~ if type(f) is Blackbox:
        # ~ return apply(getname(apply(getmethod(f,"__"),Tuple(),evr),"call"),a,evr)    # obj.__.call
    if type(f) is Baseoperating:   # 思考：别名
        return f.f(a,evr)
    elif type(f) is Function:
        return eval(f.e,updated(updated(evr,f.inevr),{f.arglname:a}))


