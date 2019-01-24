
# [require.emlobjectframe]
#

"哲学：assert是【仅当开发者出了问题】时才有效的东西"
"repr亦然"
"在面向用户的版本中"


from quickclass import localmake  # fuck fuck import

d = locals()

localmake(d,"Call",["cthead","ctl"])
localmake(d,"Cali",["clhead","cll"])
localmake(d,"Tuple",["tl"])
localmake(d,"List",["ll"])
localmake(d,"Huple",["hthead","htl"])
localmake(d,"Hist",["hlhead","hll"])

localmake(d,"Sign",["sis"])
localmake(d,"Literal",["obj"])
localmake(d,"String",["sts"])
localmake(d,"Int",["n"])
localmake(d,"Bool",["b"])

__all__ = ["Call","Cali","Sign","Literal",
"String","Int","Bool","Tuple","List","Huple","Hist"]
















