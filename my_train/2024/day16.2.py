#找到最低价值的所有路径（同一个最终值可能有多个最佳路径），把这些位置涂瓷砖，计算瓷砖数量
def right(direct):                                      #定义右转后的方向
    d = {N : E, E : S, S : W, W : N}
    return d[direct]

def left(direct):                                       #定义左转后的方向
    d = {N : W, W : S, S : E, E : N}
    return d[direct]
    
def tuple_add(a, b):                                    #元组的加减，输入当前位置和方向元组，返回下一步的位置
    return (a[0] + b[0], a[1] + b[1])

def go(field, seen):                                    #运行遍历地图
    nodes = [(len(field) - 2, 1, E, 0)]                 #初始位置在左下角起点，设为起始节点
    seen = {}                                           #经历过的节点，以及遍历到该点的最低价值(其他路径经过该点也会带有一个价值)
    results = []                                        #每到一次终点，把最终价值加入进去
    while len(nodes) != 0:                              #节点列表不为空
        node = nodes.pop(0)                             #遍历节内列表点的每一个节点，从起点开始扩散，遍历一次就把该节点删掉，价值在seen里比较
        i, j, d, v = node
 
        if i == 1 and j == len(field[0]) - 2:           #到达终点，则把价值加入results
            results.append(node[3])
            continue

        if (i, j, d) in seen and seen[(i, j, d)] < v:   #若遍历过当前位置，且之前的价值比当前到该位置的价值低，则不做处理
            continue
       
        a, b = tuple_add((i, j), d)                     #处理直行前进方向的下一步位置
        if field[a][b] != "#":      
            node = (a, b, d, v + 1)                     #不撞墙，则定义下一步节点
            if not (i, j, d) in seen or seen[(i, j, d)] > v + 1:
                seen[(i, j, d)] = v + 1                 #若未遍历过该位置，或之前遍历的该位置价值比现在的价值高，则修正该位置的最低价值 
                nodes.append(node)                      #把该节点加入节点列表

        nd = right(d)                                   #处理右转方向的下一个位置
        a, b = tuple_add((i, j), nd)
        if field[a][b] != "#":
            node = (a, b, nd, v + 1001)                 #转了弯，价值加1001
            if not (i, j, nd) in seen or seen[(i, j, nd)] > v + 1001:
                seen[(i, j, nd)] = v + 1001
                nodes.append(node)

        nd = left(d)                                    #同上
        a, b = tuple_add((i, j), nd)
        if field[a][b] != "#":
            node = (a, b, nd, v + 1001)
            if not (i, j, nd) in seen or seen[(i, j, nd)] > v + 1001:
                seen[(i, j, nd)] = v + 1001
                nodes.append(node)

    return min(results),seen
def trace_back(pathvalue, bearing, coord, seen, places):
    places.add(coord)                                                             #先把当前位置加入places

    if pathvalue == 0:                                                            #如果值为0，则到达了起点，循环终止
        return
    
    a, b = tuple_add(coord, right(right(bearing)))                                #方向改成相反，直接两次右转反转，得到下一步位置
    if (a, b, bearing) in seen and seen[(a, b, bearing)] == pathvalue - 1:        #确定该位置在seen里，且价值为现有价值减去步长增加价值
        trace_back(pathvalue - 1, bearing, (a, b), seen, places)                  #回溯下一步位置

    right_direct = right(bearing)                                                 #同理算出后面左转和右转的方向
    left_direct = left(bearing)                                      

    a, b = tuple_add(coord, right_direct)                                                #注意：加的是右转的方向（只是算回溯的坐标），下面的位置方向是左转
    if (a, b, left_direct) in seen and seen[(a, b, left_direct)] == pathvalue - 1001:
        trace_back(pathvalue - 1001, left_direct, (a, b), seen, places)

    a, b = tuple_add(coord, left_direct)
    if (a, b, right_direct) in seen and seen[(a, b, right_direct)] == pathvalue - 1001:
        trace_back(pathvalue - 1001, right_direct, (a, b), seen, places)


# global variables
N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
seen = {}

# get input
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input16.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
    field=[[s for s in line] for line in lines]

# walk the field
pathvalue,seen = go(field, seen)                                                    #先遍历完找到最低价值和遍历的每个位置的价值的seen
pathvalue+=1                                                                        #多加一个1，回溯的时候会多减一个

# trace back ways
places = set()
trace_back(pathvalue, E , (1, len(field) - 2), seen, places)                        #到终点时候的价值，方向，位置，seen和回溯匹配的位置集
result = len(places)

# print result
print(result)