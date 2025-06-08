#在一个地图里，按照方向前进，遇到障碍物就右转，把每一步路径变为X，求出去后有多少个X
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input6.txt",mode="r",encoding="utf-8") as f:
    str=f.read()
lines=str.strip().split("\n")
map=[list(line) for line in lines]          #生成地图矩阵
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col]=="^":
            x=row                           #查找初始位置
            y=col
            break
while True:
    idx=x                                   #定义下一步的位置idx，idy
    idy=y
    if map[x][y]=="^":                      #判断前进方向以及下一步的方向及位置
        idx=x-1
        next=">"
    elif map[x][y]==">":
        idy=y+1
        next="v"
    elif map[x][y]=="v":
        idx=x+1 
        next="<"
    elif map[x][y]=="<":
        idy=y-1
        next="^"
    if idx<0 or idx>=len(map) or idy<0 or idy>=len(map[0]):    #判断下一步是否会走出地图范围
        break
    elif map[idx][idy]=="#":                                   #遇到障碍物，改变方向
        map[x][y]=next
    else:
        map[idx][idy]=map[x][y]                                #没有障碍物，移动到下一个位置，并把原来位置变成X，同时重新赋值x,y的新位置
        map[x][y]="X"
        x=idx
        y=idy
map[x][y]="X"                                                  #下一步会走出地图时，把现在所在位置也变成X表示走出去了，
count=0
for i in range(len(map)):
      for j in range(len(map[0])):
         if map[i][j]=="X":
               count+=1          
print(count)