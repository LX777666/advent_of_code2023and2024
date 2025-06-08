#推箱子游戏，挪动的箱子前进方向有接触其他箱子，则一起挪动
def move_O(x,y,dx,dy,map):
    for i in range(1,max(len(map),len(map[0]))):                 #移动箱子函数，先探索能否移动以及移动的距离n，会返回一个值n
            tempx=x+i*dx
            tempy=y+i*dy
            if map[tempx][tempy]=="#":
                n=0
                break
            elif map[tempx][tempy]==".":
                n=i
                break
            elif map[tempx][tempy]=="O":
                continue
    if n!=0:                                                     #根据n来挪动箱子  
       map[x][y]="."
       map[x+dx][y+dy]="@"
       for i in range(2,n+1):
          map[x+i*dx][y+i*dy]="O"
    return n
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input15a.txt",mode="r",encoding="utf-8") as f1:  #读取map
    lines=f1.read().strip().split("\n")
    map=[[s for s in line]  for line in lines]
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input15b.txt",mode="r",encoding="utf-8") as f2:  #读取行动方向
    str1=f2.read().strip()
    move=[s for s in str1]
    num=move.count("\n")                                                                 #删除换行符
    for i in range(num):
        move.remove("\n")
for i in range(len(map)):                                                                #找到初始位置
    for j in range(len(map[0])):
        if map[i][j]=="@":
            x=i
            y=j
directions={"<":(0,-1),"^":(-1,0),">":(0,1),"v":(1,0)}                                   #设置方向
for i in range(len(move)):
    n=0
    dx=directions[move[i]][0]
    dy=directions[move[i]][1]
    nx=x+dx                                    #下一步位置
    ny=y+dy
    if map[nx][ny]=="#":
        continue
    elif map[nx][ny]==".":
        map[nx][ny]="@"
        map[x][y]="."
        n=1                                    #返回不为0的n表示挪动过，需要重新设置初始位置x，y
    elif map[nx][ny]=="O":                     #遇到箱子则调用挪箱子函数
        n=move_O(x,y,dx,dy,map)
    if n!=0:
      x=nx
      y=ny
count=0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]=="O":
            count+=i*100+j
print(count)