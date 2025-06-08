#在一个字符地图里，按照水平垂直倒退对角的方向，判断是否有XMAS
import re
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input4.txt",mode="r",encoding="utf-8") as f:
    res=f.read()
lines=res.strip().split("\n")                                   #把字符串里面的每一行（按\n分割）作为一个字符串放入列表内即["sdadad","dasdws","saaawf"]
matrix=[list(line) for line in lines]                           #把列表中的每一个元素(字符串)变成列表，再在外面套了一个列表[]即成了二维列表
count=0
#水平查找
for row in matrix:                                             #XMAS
    if "XMAS" in ''.join(row):
      count+=''.join(row).count("XMAS")
    if "SAMX" in ''.join(row):  # 倒退检查
      count+=''.join(row).count("SAMX")
#垂直查找
for col in range(len(matrix[0])):            
    column="".join([matrix[row][col] for row in range(len(matrix))])   #把每一列的所有元素拼接起来成一个字符串
    if "XMAS" in column:
      count+=column.count("XMAS")
    if "SAMX" in column:  # 倒退检查
      count+=column.count("SAMX")
#对角查找
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if row+len("XMAS")<=len(matrix) and col+len("XMAS")<=len(matrix[0]):       #设定行、列的范围
             diag="".join([matrix[row+i][col+i] for i in range(len("XMAS"))])      #正对角线，把满足范围的对角线元素拼接成一个字符串  
             if "XMAS" in diag:
               count+=diag.count("XMAS")
             if "SAMX" in diag:  # 倒退检查
               count+=diag.count("SAMX")
        if row+len("XMAS")<=len(matrix) and col-len("XMAS")+1>=0:                  #反对角线
              diag="".join([matrix[row+i][col-i] for i in range(len("XMAS"))])
              if "XMAS" in diag:
                count+=diag.count("XMAS")
              if "SAMX" in diag:  # 倒退检查
                count+=diag.count("SAMX")
print(count)