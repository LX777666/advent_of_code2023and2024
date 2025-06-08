#对判断排序错误的数据进行修改，按照规则重新排序后，把每行排在中间的数据加起来
import re
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input5a.txt",mode="r",encoding="utf-8") as f:  #把规则和数据分成两个txt文件，提取规则
    f1=f.readlines()                                                                   #读取每一行
rule=[]
for line in f1:                                                                        
    res=re.findall("\d+",line)                                                         #在每一行中找数字，得到一个两位列表
    rule.append(res)                                                                   #把每行列表加入rule中，形成矩阵
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input5b.txt",mode="r",encoding="utf-8") as f2:
    f2=f2.readlines()                                                                  #读取数据
def correct(rule,line):
    for i in range(len(rule)):
        if rule[i][0] in line and rule[i][1] in line:                                  
            if line.index(rule[i][0])<line.index(rule[i][1]):      #排序正常则继续下个循环
               continue                                                                 
            else:                                                  #不正确则将两个数据交换位置，然后重新调用correct函数嵌套重新验证交换顺序之后的line，直到所有的都符合顺序
               index1=line.index(rule[i][0])
               index2=line.index(rule[i][1])
               temp=rule[i][0]
               line[index1]=line[index2]
               line[index2]=temp
               correct(rule,line)
    return 1                                                       #返回1
sum=0 
for line in f2:
   line=line.strip().split(",")                                                        #每一行按，分割成列表
   flag=1                                                                              #定义flag标志
   for i in range(len(rule)):
       if rule[i][0] in line and rule[i][1] in line:                                   #如果rule[i]的两个数字在line中，则该规则可应用
           if line.index(rule[i][0])<line.index(rule[i][1]):                           #判断规则的两个数字在line的排序是否符合规则
               continue                                                                 
           else:
               flag=0                                                                  #标志为错误排序
               correct(rule,line)                                                      #调用correct函数修改
   if flag==0:         
     sum+=int(line[len(line)//2])                                                     #把正确数据中间的数字加起来
print(sum)    
           