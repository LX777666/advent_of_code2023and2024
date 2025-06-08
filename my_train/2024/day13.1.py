#抓娃娃机有AB两个按钮，每个按钮费用不同，可以让x y按一定步长增加，x y同时达到某个值才能中奖，问中奖的最低费用
import re
def win(res1,res2,res3):                             #中奖函数
    Ax=int(res1[0])
    Ay=int(res1[1])
    Bx=int(res2[0])
    By=int(res2[1])
    X=int(res3[0])
    Y=int(res3[1])
    reach=[]
    for i in range(1,101):
       for j in range(1,101):                       #xy只要有一个超出范围则立刻break
          if i*Ax+j*Bx>X or i*Ay+j*By>Y:
              break
          if i*Ax+j*Bx==X and i*Ay+j*By==Y:
              reach.append([i,j])                   #把中奖的i，j保存下来，方便后续找出最低费用
    if len(reach)==0:
        return 0                                    #未中奖直接返回0
    else:
       res=reach[0][0]*3+reach[0][1]                #先设置中奖费用初始值 
       for i in range(len(reach)):
           price=reach[i][0]*3+reach[i][1] 
           res=min(price,res)                       #筛选最低费用
       return res      
      
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input13.txt",mode="r",encoding="utf-8") as f:
    f1=f.read().split("\n")                         #按行划分，到一个列表
    n=f1.count("")                                  #算出空白行的个数
for i in range(n): 
    f1.remove("")                                   #按照个数删除掉列表的空白元素
price=0 
for i in range(0,len(f1),3):
    res1 = re.findall("\d+",f1[i])                  #找出每行的数字，i的步长为3
    res2 = re.findall("\d+",f1[i+1])
    res3 = re.findall("\d+",f1[i+2])
    price+=win(res1,res2,res3)
print(price)