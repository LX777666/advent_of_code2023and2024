#把一个两列的数据分成两半，然后按照从小到大的顺序分别计算两个列表的差值，最后累加起来
import os
try:
   os.makedirs(r"C:\\Users\\lxlaptop\\Desktop\\input\\input1.txt")  #创建文件路径
except FileExistsError:
   print("文件已存在") 
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input1.txt",mode="r",encoding="utf-8") as f:
   list1=[]
   list2=[]
   for line in f:
      line=line.strip().split()         #把文件每行分成列表的形式，然后分别加在两个列表里面
      list1.append(line[0])
      list2.append(line[1])
list1.sort()                            #排序
list2.sort()
sum=0
for i in range(len(list2)):
   sum+=abs(int(list1[i])-int(list2[i]))
print(sum)

