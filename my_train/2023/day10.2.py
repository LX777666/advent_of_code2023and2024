#找到loop围成的图形内部的点的个数
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
     elif map[x][y]=="S":              #遇到S也一样返回1
        return x,y,direction,map,flag
     else:
       flag=0
       return x,y,direction,map,flag
    else:
       flag=0
       return x,y,direction,map,flag
def go(x,y,map):                     #进行遍历
    nodes=[]                         #节点列表，用于存储两个方向上的下一个位置
    for direction in directions:     #只找到起点的一个方向
       i,j,direction1,map,flag=next(x,y,direction,map)
       if flag==1:
          nodes.append((x,y,direction))
          break
    seen = [(x,y)]                   #经历过的节点，以及遍历到该点的步长
    while len(nodes)!=0:             #节点列表不为空
        node = nodes.pop(0)          #遍历两个方向的每一个节点，实时更新
        i,j,d=node
        i,j,direction,map,flag=next(i,j,d,map)
        if (i,j) in seen and (i,j)==(x,y):   #若已经遍历过该位置，并且该位置是起点，则break
           return seen
        if flag==0:
           print("出错")
           return 0
        seen.append((i,j))
        nodes.append((i,j,direction))   #更新节点

import math
from collections import deque
def pick_theorem(polygon):
    """
    使用 Picks 定理计算多边形内部点数
    :param polygon: 多边形顶点坐标列表，按顺序排列 [(x1,y1), (x2,y2), ..., (xn,yn)]
    :return: 内部点数
    """
    # 1. 计算多边形面积(A)-使用鞋带公式
    area=shoelace_area(polygon)

    # 2. 计算边界点数 (B)
    boundary_points=count_boundary_points(polygon)

    # 3. 应用 Picks 定理: A = I + B/2 - 1
    # => I = A - B/2 + 1
    internal_points=area-boundary_points//2+1

    return internal_points

def shoelace_area(polygon):
    """计算多边形面积（鞋带公式）"""
    n=len(polygon)
    area=0
    for i in range(n):
        x_i,y_i=polygon[i]
        x_j,y_j=polygon[(i+1)%n]
        area+=(x_i*y_j)-(x_j*y_i)
    return abs(area)/2

def count_boundary_points(polygon):
    """计算多边形边界上的整数点数"""
    n=len(polygon)
    boundary_count=0

    for i in range(n):
        x1,y1=polygon[i]
        x2,y2=polygon[(i+1)%n]

        # 计算当前边上的点数（包括端点）
        dx=abs(x2-x1)
        dy=abs(y2-y1)
        gcd_val=math.gcd(dx,dy)

        # 每条边上的点数 = gcd(dx,dy) + 1
        # 但为了避免重复计算顶点，我们减去1
        boundary_count+=gcd_val

    return boundary_count
with open("C:\\Users\\sage\\Desktop\\train\\input2\\input10.txt", "r") as f:
    lines=f.read().strip().split("\n")
map=[[x for x in line] for line in lines]
directions={"^":(-1,0),"↓":(1,0),"<":(0,-1),">":(0,1)}
x,y=get_start(map)
seen=go(x,y,map)
print(pick_theorem(seen))