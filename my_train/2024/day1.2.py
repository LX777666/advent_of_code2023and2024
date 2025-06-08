#两列数据，左边一列的数据乘以该数据在右列出现的次数再累加起来
import os
try:
   os.makedirs(r"C:\\Users\\lxlaptop\\Desktop\\input\\input1.txt")  #创建文件路径
except FileExistsError:
   print("文件已存在") 
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input1.txt",mode="r",encoding="utf-8") as f:
   list1=[]
   list2=[]
   for line in f:
      line=line.strip().split()
      list1.append(line[0])
      list2.append(line[1])
sum=0
for i in range(len(list1)):
   num=0
   for j in range(len(list2)):
      if list1[i]==list2[j]:
         num+=1 
   sum+=num*int(list1[i])              #list[i]是字符串类型，需要加一个int()
print(sum)