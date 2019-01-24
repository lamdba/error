
# [require.el1objectframe]
#

"哲学：assert是【仅当开发者出了问题】时才有效的东西"
"repr亦然"
"在面向用户的版本中"


from quickclass import localmake  # fuck fuck import

d = locals()

localmake(d,"Call",["cthead","ctl"])
localmake(d,"Cali",["clhead","cll"])
localmake(d,"Sign",["sis"])
localmake(d,"Literal",["obj"])

localmake(d,"String",["sts"])
localmake(d,"Int",["n"])
localmake(d,"Bool",["b"])
localmake(d,"Tuple",["tl"])
localmake(d,"List",["ll"])
localmake(d,"Huple",["hthead","htl"])
localmake(d,"Hist",["hlhead","hll"])

localmake(d,"Blackbox",["fields","methods"])# 方法不同于函数，方法要同时接受参数列表和字段空间2个东西
localmake(d,"Namespace",["d"])
localmake(d,"A",["l"])  # /Names/Hint
localmake(d,"Baseoperating",["f"])
localmake(d,"Function",["arglname","e","inevr"])  # 应当完全闭包

__all__ = ["Call","Cali","Sign","Literal",
"String","Int","Bool","Tuple","List","Huple","Hist",
"Blackbox","Namespace","A","Baseoperating","Function"]















