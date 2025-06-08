#在地图内按照符号管道进行移动，会进入一个循环loop，找到离起点S最远的点的步数
def get_start(map):                   #找到起点的位置
  for i in range(len(map)):
     for j in range(len(map[0])):
        if map[i][j]=="S":
            return i,j
def tuple_add(a,b):                   #进行元组加减
   return (a[0]+b[0],a[1]+b[1])

def next(x,y,direction,map):          #根据当前位置和方向找到下个位置，并根据下个位置的符号找到新的方向
    flag=1                            #若管道对接出错，返回flag为0
    a=(x,y)
    b=directions[direction]
    new_location=tuple_add(a,b)
    x=new_location[0]
    y=new_location[1]
    if 0<=x<len(map) and 0<=y<len(map[0]):
     if map[x][y]=="|":
       if direction=="^":
          direction="^"
       elif direction=="↓":
          direction="↓"
       else:
          flag=0
       return x,y,direction,map,flag
     elif map[x][y]=="-":
       if direction==">":
          direction=">"
       elif direction=="<":
          direction="<"
       else:
          flag=0
       return x,y,direction,map,flag
     elif map[x][y]=="7":
       if direction==">":
          direction="↓"
       elif direction=="^":
          direction="<"
       else:
          flag=0
       return x,y,direction,map,flag
     elif map[x][y]=="L":
       if direction=="<":
          direction="^"
       elif direction=="↓":
          direction=">"
       else:
          flag=0
       return x,y,direction,map,flag
     elif map[x][y]=="J":
       if direction==">":
          direction="^"
       elif direction=="↓":
          direction="<"
       else:
          flag=0
       return x,y,direction,map,flag
     elif map[x][y]=="F":
       if direction=="<":
          direction="↓"
       elif direction=="^":
          direction=">"
       else:
          flag=0
       return x,y,direction,map,flag
     elif map[x][y]==".":
          flag=0
          return x,y,direction,map,flag
    else:
       return x,y,direction,map,flag
def go(x,y,map):                     #进行遍历
    nodes=[]                         #节点列表，用于存储两个方向上的下一个位置
    for direction in directions:     #找到起点的两个出发方向并存入节点列表中
       i,j,direction1,map,flag=next(x,y,direction,map)
       if flag==1:
          nodes.append((x,y,direction,0))
    seen = {(x,y):0}                 #经历过的节点，以及遍历到该点的步长
    while len(nodes)!=0:             #节点列表不为空
        node = nodes.pop(0)          #遍历两个方向的每一个节点，实时更新
        i,j,d,v=node
        i,j,direction,map,flag=next(i,j,d,map)
        if (i,j) in seen and (i,j)!=(x,y):   #若已经遍历过该位置，并且该位置不是起点，则该位置为最远距离
           print (seen[(i,j)])
           break
        if flag==0:
           continue
        seen[(i,j)]=v+1              #记录每个位置的步长
        nodes.append((i,j,direction,v+1))  #更新节点

with open("C:\\Users\\sage\\Desktop\\train\\input2\\input10.txt", "r") as f:
    lines=f.read().strip().split("\n")
map=[[x for x in line] for line in lines]
directions={"^":(-1,0),"↓":(1,0),"<":(0,-1),">":(0,1)}
x,y=get_start(map)
go(x,y,map)