#两部分元素，一部分x，y加编号和对应值，然后根据另一部分的表达式判断进行并、异或、或等计算
#最后将z开头的符号的值进行提取，然后按照编号来拼接成一个二进制数，判断该数的十进制值
import re
def caculate(a,op,b,c,d):                           #定义函数，根据op进行不同计算，并将结果存入d字典内
    if op=="AND":
        result=d[a] and d[b]
    if op=="XOR":
        result=d[a] ^ d[b]
    if op=="OR":
        result=d[a] or d[b]
    d[c]=result

with open("C:\\Users\\lxlaptop\\Desktop\\input\\input24a.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
d={}
for line in lines:                                  #文件1里面的键值对，直接存入d字典中
    res=re.findall("\w+",line)
    d[res[0]]=int(res[1])    
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input24b.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
temp=[]
for line in lines:
    res=re.findall("\w+",line)
    if res[0] in d and res[2] in d:                          #文件2中的字符，首先得判断将要计算的符号是否已经在字典中有相应的值
        caculate(res[0],res[1],res[2],res[3],d)              #若有则计算，没有则暂存如temp中后续处理
    else :
        temp.append(res)
while temp!=[]:                                              #直到清空temp才停止
    for res in temp:                                         #不断用更新后的d去判断并计算temp中的符号
      if res[0] in d and res[2] in d:
        caculate(res[0],res[1],res[2],res[3],d)
        temp.remove(res)                                     #计算完后，将temp中的该值移除 
zd={}                                                        #创建一个z开头的字典，方便存储进行操作
for key in d:                                             
    if key.startswith("z"):                                  #判断是否以z开头
       zd[key]=str(d[key])                                   #将值变成字符串的形式存入字典，方便后续拼接
zdkey = sorted(zd.keys(), reverse=True)                      #按照逆序对zd的键进行排序
result=""                                                    #初始化拼接的结果
for item in zdkey:        
   result=result+zd[item]                                    #按顺序把zd的每一个值拼接
result=int(result,2)                                         #最后用int从二进制转换为十进制数
print(result)  