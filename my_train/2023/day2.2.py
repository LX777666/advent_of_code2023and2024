#计算每一个game中若可能所需要的最少的每种颜色个数，并累乘为它的power并累加起来
import re
def power(grabs):
    cubes={"green":0,"red":0,"blue":0}      #初始化cubes 
    for grab in grabs:                      #遍历grabs中每一个grab
      res=re.findall("\w+",grab)
      dict={}
      keys={"red","green","blue"}           #设置dict数组默认三种颜色的个数为0，以防grab中缺少某种颜色，导致字典键缺失
      for key in keys:
        dict.setdefault(key, 0)
      for i in range(0,len(res),2):         #把grab中的颜色和对应个数加入到dict中
        dict[res[i+1]]=int(res[i])   
      if dict["red"]>cubes["red"]:          #更新最大的cube值
         cubes["red"]=dict["red"]
      if dict["green"]>cubes["green"]:
         cubes["green"]=dict["green"]
      if dict["blue"]>cubes["blue"]:
         cubes["blue"]=dict["blue"]
    power=cubes["red"]*cubes["blue"]*cubes["green"]  #计算并返回power
    return power
result=0
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input2.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
for line in lines:                    #按照:分割，方便后面对grabs进行处理(防止多一个键game)
    line=line.split(":")
    grabs=line[1].split(";")          #按照:分割成不同的grab
    res=power(grabs)                  #计算power并累加
    result+=res
print(result)

    