#判断字符地图里是否有MAS按照形状摆放，即A在中间，在其正副对角线上有两个MAS，形状像一个X
import re
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input4.txt",mode="r",encoding="utf-8") as f:
    res=f.read()
lines=res.strip().split("\n")                                   #把字符串里面的每一行（按\n分割）作为一个字符串放入列表内即["sdadad","dasdws","saaawf"]
matrix=[list(line) for line in lines]                           #把列表中的每一个元素(字符串)变成列表，再在外面套了一个列表[]即成了二维列表
count=0
def isX(matrix,row,col):                                        #定义一个函数，判断该位置的A的对角是不是MS呈X形状
    if matrix[row-1][col-1]=="M" :
        if matrix[row-1][col+1]=="M":
            if matrix[row+1][col+1]=="S" and matrix[row+1][col-1]=="S": 
                return 1
        elif matrix[row+1][col-1]=="M":
            if matrix[row+1][col+1]=="S" and matrix[row-1][col+1]=="S": 
                return 1
    elif matrix[row+1][col+1]=="M" :
        if matrix[row-1][col+1]=="M":
           if matrix[row-1][col-1]=="S" and matrix[row+1][col-1]=="S": 
                return 1
        elif matrix[row+1][col-1]=="M":
            if matrix[row-1][col+1]=="S" and matrix[row-1][col-1]=="S": 
                return 1
    else:
        return 0
#对角查找
for row in range(len(matrix)-1):                    #确定范围，不能取到矩阵边缘
    for col in range(len(matrix[0])-1):
       if row>=1 and col >=1 :
           if matrix[row][col]=="A":
            if isX(matrix,row,col):
                count+=1
       else:
           continue
               
print(count)