#根据提供的bag中的每种cube的个数，判断每一个game是否可能成立，将成立的game的编号加起来
import re
def ispossible(grabs,bag):          #判断是否可能
    for grab in grabs:              #遍历每一次抓取的grab
      res=re.findall("\w+",grab)
      dict={}                 
      keys={"red","green","blue"}   #设置每种键的默认值为0，防止因grab缺少某种颜色，出现键的缺失报错
      for key in keys:              
        dict.setdefault(key, 0)     
      for i in range(0,len(res),2): #把grab中的每种颜色和个数加入到dict中
        dict[res[i+1]]=int(res[i])   
      if dict["red"]>bag["red"] or dict["green"]>bag["green"] or dict["blue"]>bag["blue"]:  #若有一种颜色的个数大于bag的个数，则不可能，直接返回0
         return 0
    return 1                        #可能，返回1
bag={"green":13,"red":12,"blue":14}
result=0
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input2.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
for line in lines:
    line=line.split(":")           #按照：分割开，方便找到game的编号，并对另一部分进行处理
    res=re.findall("\w+",line[0])
    num=int(res[1])
    grabs=line[1].split(";")
    if ispossible(grabs,bag):      #判断该game的grabs是否可能
       result+=num
print(result)

    