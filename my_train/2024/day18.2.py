#判断哪个障碍物坐标添加进去后，地图不存在到达终点的路径
import re
def right(direct):                                      #定义右转后的方向
    d = {N : E, E : S, S : W, W : N}
    return d[direct]

def left(direct):                                       #定义左转后的方向
    d = {N : W, W : S, S : E, E : N}
    return d[direct]
    
def tuple_add(a, b):                                    #元组的加减，输入当前位置和方向元组，返回下一步的位置
    return (a[0] + b[0], a[1] + b[1])

def go(map, seen):                                      #运行遍历地图
    nodes = [(0, 0, E, 0)]                              #初始位置在左上角起点，设为起始节点
    seen = {}                                           #经历过的节点，以及遍历到该点的最低步长(其他路径经过该点也会带有一个步长)
    results = []                                        #results空列表，每到一次终点，把最终步长加入进去
    while len(nodes) != 0:                              #节点列表不为空
        node = nodes.pop(0)                             #遍历节内列表点的每一个节点，从起点开始扩散，遍历一次就把该节点删掉，步长在seen里比较
        i, j, d, v = node
 
        if i == 70 and j == 70:                         #到达终点，则把步长加入results
            results.append(node[3])
            continue

        if (i, j, d) in seen and seen[(i, j, d)] < v:   #若遍历过当前位置，且之前的步长比当前到该位置的步长低，则不做处理
            continue
       
        a, b = tuple_add((i, j), d)                     #处理直行前进方向的下一步位置
        if 0<=a<len(map) and 0<=b<len(map[0]) and map[a][b] != "#" :      
            node = (a, b, d, v + 1)                     #不撞墙，则定义下一步节点
            if not (i, j, d) in seen or seen[(i, j, d)] > v + 1:
                seen[(i, j, d)] = v + 1                 #若未遍历过该位置，或之前遍历的该位置步长比现在的步长高，则修正该位置的最低步长 
                nodes.append(node)                      #把该节点加入节点列表

        nd = right(d)                                   #处理右转方向的下一个位置
        a, b = tuple_add((i, j), nd)
        if 0<=a<len(map) and 0<=b<len(map[0]) and map[a][b] != "#" :  
            node = (a, b, nd, v + 1)                    #转了弯，重新定义方向，步长也加1
            if not (i, j, nd) in seen or seen[(i, j, nd)] > v + 1:
                seen[(i, j, nd)] = v + 1
                nodes.append(node)

        nd = left(d)                                    #同上
        a, b = tuple_add((i, j), nd)
        if 0<=a<len(map) and 0<=b<len(map[0]) and map[a][b] != "#" :  
            node = (a, b, nd, v + 1)
            if not (i, j, nd) in seen or seen[(i, j, nd)] > v + 1:
                seen[(i, j, nd)] = v + 1
                nodes.append(node)
    if results==[]:                                   #若找不到出去的路径，则返回0
        return 0
    else:
        return min(results)                           #返回出去路径中的最小步长

N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)         #定义方向的移动模式
map=[["." for _ in range(71)] for _ in  range(71)]    #先创建一个71X71的地图，都填入“.”
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input18.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")                #每行字符串作为一个列表元素
    for i in range(1024):                             #先把前1024行的坐标进行转换，按坐标在map里添加障碍物
        res=re.findall("\d+",lines[i])
        map[int(res[0])][int(res[1])]="#"
i=1024                                                #定义lines的读取起点
while True:                                           #循环遍历，查找第一个让路径无法到达终点的障碍物坐标 
   seen={}
   res=re.findall("\d+",lines[i])
   map[int(res[0])][int(res[1])]="#"
   result = go(map,seen)
   if result==0:
       print(int(res[0]),",",int(res[1]))
       break
   else:
       i+=1