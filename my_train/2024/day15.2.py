#现在把map扩宽，箱子变成[]也有两个角，任意一个角都可以推动箱子
from copy import deepcopy
def can_move(tempx,tempy,dx,dy,new_map):                           #判断能否移动，(输入的是下一步的位置，并且已经知道该位置是箱子了)
    if new_map[tempx][tempy]=="[":                                 #判断是箱子左侧还是右侧
        py=1
    if new_map[tempx][tempy]=="]":
        py=-1
    tempx+=dx                                                      #再判断下一步位置
    tempy+=dy
    if new_map[tempx][tempy]=="#" or new_map[tempx][tempy+py]=="#":    #若为障碍物，只要有一个障碍物，直接返回1结束
        return 1
    if new_map[tempx][tempy]=="." and new_map[tempx][tempy+py]==".":   #两个都是空格才返回0   
        return 0
    result=0                                                           #定义result为0，所有分支都有空位能移动，最终result才为0
    if new_map[tempx][tempy]=="[" or new_map[tempx][tempy]=="]":       #加上每个分支的返回值
        result+=can_move(tempx,tempy,dx,dy,new_map)
    if new_map[tempx][tempy+py]=="[" or new_map[tempx][tempy+py]=="]":
        result+=can_move(tempx,tempy+py,dx,dy,new_map)  
    return result
def box_move(x,y,dx,dy,new_map,temp_map,path):                         #移动箱子
    new_map[x+dx][y+dy]=temp_map[x][y]                                 #先把当前位置的箱子挪动，默认挪箱子左下角，每次挪动都是把两边一起挪
    new_map[x+dx][y+dy+1]=temp_map[x][y+1]                       
    path.append([x,y])                                                 #把挪动箱子的原来位置存入path
    path.append([x,y+1])
    if [x-dx,y-dy+1]  in path:                                         #如果原来位置的前一个位置在path中，说明是需要挪动的，即把原来位置变成前一个位置的元素
         new_map[x][y+1]=temp_map[x-dx][y-dy+1]                        #若不在path中，说明不会挪动，则当前位置箱子挪完后在当前位置补"."
    else:
         new_map[x][y+1]="."
    if [x-dx,y-dy]  in path:
         new_map[x][y]=temp_map[x-dx][y-dy]
    else:
         new_map[x][y]="."
    if temp_map[x+dx][y+dy]=="[" and temp_map[x+dx][y+dy+1]=="]":      #若下一个位置的元素为[或者]，则说明也是箱子需要挪动，三种情况
        box_move(x+dx,y+dy,dx,dy,new_map,temp_map,path)                #[]与原来位置的[]刚好对上，则只需要挪动新箱子左下角即可
    if temp_map[x+dx][y+dy]=="]":                                      #若当前箱子的[与下一步位置箱子的]对上，则box_move函数的位置要变成这个箱子的左下角[的位置
        box_move(x+dx,y+dy-1,dx,dy,new_map,temp_map,path)
    if temp_map[x+dx][y+dy+1]=="[":                                    #同上
        box_move(x+dx,y+dy+1,dx,dy,new_map,temp_map,path)
def move_O(x,y,dx,dy,new_map):                                #挪箱子
    if dx==0:                                                 #如果左右移动则只需要判断左右方向是否有空位，然后把所有箱子位移即可
     for i in range(1,max(len(new_map),len(new_map[0]))):     #从1步开始，探索前方是否有空格位置
            tempx=x+i*dx     
            tempy=y+i*dy
            if new_map[tempx][tempy]=="#":                    #只要遇到障碍物，直接返回0
               return 0
            elif new_map[tempx][tempy]==".":                  #若找到空格，即令n等于i，方便挪箱子
                n=i
                break
            elif new_map[tempx][tempy]=="[" or new_map[tempx][tempy]=="]":
                continue   
     if n!=0:                                                 #n不为0，开始变换位置
       for i in range(n,1,-1):                                #每个位置位移一步，最后把初始位置变成".",第一步位置变为@
          new_map[x+i*dx][y+i*dy]=new_map[x+i*dx-dx][y+i*dy-dy]
       new_map[x][y]="."
       new_map[x+dx][y+dy]="@"
     return n                                                 #返回n(不为0就行)
    elif dy==0:                                               #若上下方向移动
        n=0
        tempx=x+dx                                            #尝试下一步位置
        tempy=y+dy
        if can_move(tempx,tempy,dx,dy,new_map)==0:            #先判断能否移动
            n=1
            temp_map=deepcopy(new_map)                        #先复制一个该地图，在这个地图上进行遍历判断
            path=[]
            if new_map[tempx][tempy]=="[":
                box_move(tempx,tempy,dx,dy,new_map,temp_map,path)
                new_map[tempx][tempy]="@"
                new_map[tempx][tempy+1]="."     
                new_map[x][y]="."   
            if new_map[tempx][tempy]=="]":
                box_move(tempx,tempy-1,dx,dy,new_map,temp_map,path)
                new_map[tempx][tempy]="@"
                new_map[tempx][tempy-1]="."     
                new_map[x][y]="."                                   #初始位置变为"."
        return n
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input15a.txt",mode="r",encoding="utf-8") as f1:
    lines=f1.read().strip().split("\n")
    map=[[s for s in line]  for line in lines]                             #提取文件地图 
new_map = [[0 for _ in range(2*len(map[0]))] for _ in range(len(map))]     #初始化地图
for i in range(len(map)):                                                  #将地图变宽
        for j in range(len(map[0])):
            if map[i][j]=="#":
                new_map[i][2*j]="#"
                new_map[i][2*j+1]="#"
            elif map[i][j]==".":
                new_map[i][2*j]="."
                new_map[i][2*j+1]="."
            elif map[i][j]=="O":
                new_map[i][2*j]="["
                new_map[i][2*j+1]="]"
            elif map[i][j]=="@":
                new_map[i][2*j]="@"
                new_map[i][2*j+1]="."
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input15b.txt",mode="r",encoding="utf-8") as f2:   
    str1=f2.read().strip()
    move=[s for s in str1]                               #读取行动方向
    num=move.count("\n")                                 #除去方向里面的回车
    for i in range(num):
        move.remove("\n")                                
for i in range(len(new_map)):                            #找到起点@位置
    for j in range(len(new_map[0])):
        if new_map[i][j]=="@":
            x=i
            y=j
directions={"<":(0,-1),"^":(-1,0),">":(0,1),"v":(1,0)}   #定义方向字典，value为下一步行动
for i in range(len(move)):                               #遍历行动
    n=0
    dx=directions[move[i]][0]
    dy=directions[move[i]][1]
    nx=x+dx                                              #下一步位置
    ny=y+dy
    if new_map[nx][ny]=="#":                             #下一步位置为障碍物，不行动
        continue
    elif new_map[nx][ny]==".":                           #下一步位置为空白，前进
        new_map[nx][ny]="@"
        new_map[x][y]="."
        n=1                                              #记录行动了，方便后面重新初始化起点位置
    elif  new_map[nx][ny]=="[" or new_map[nx][ny]=="]" : #下一步位置为箱子
        n=move_O(x,y,dx,dy,new_map)                      #启用挪箱子move_O函数，并返回n
    if n!=0:
      x=nx
      y=ny
count=0
for i in range(len(new_map)):
    for j in range(len(new_map[0])):
        if new_map[i][j]=="[":
            count+=i*100+j
print(count)
