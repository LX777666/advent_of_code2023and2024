#一个规则数据，每行两个数字，规则为要求排序时前面的数字必须排在后面的数字的前面
#一个n行数据，判断每行数据是否排序正确，若正确则将排在中间的数字加起来
import re
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input5a.txt",mode="r",encoding="utf-8") as f:  #把规则和数据分成两个txt文件，提取规则
    f1=f.readlines()                                                                   #读取每一行
rule=[]
for line in f1:                                                                        
    res=re.findall("\d+",line)                                                         #在每一行中找数字，得到一个两位列表
    rule.append(res)                                                                   #把每行列表加入rule中，形成矩阵
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input5b.txt",mode="r",encoding="utf-8") as f2:
    f2=f2.readlines()                                                                  #读取数据
sum=0 
for line in f2:
   line=line.strip().split(",")                                                        #每一行按，分割成列表
   flag=1                                                                              #定义flag标志
   for i in range(len(rule)):
       if rule[i][0] in line and rule[i][1] in line:                                   #如果rule[i]的两个数字在line中，则该规则可应用
           if line.index(rule[i][0])<line.index(rule[i][1]):                           #判断规则的两个数字在line的排序是否符合规则
               flag=1                                                                  
           else:
               flag=0                                                                  #不符合规则则跳出循环。看下一行数据
               break
   if flag:
      sum+=int(line[len(line)//2])                                                     #把正确数据中间的数字加起来
print(sum)    
           