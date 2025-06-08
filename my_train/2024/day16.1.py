#在一个地图里面找到到终点的值，每前进一步值加1，每转一次方向值加1000，求最低值
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

    return min(results)


# global variables
N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)

# get input
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input16.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
    field=[[s for s in line] for line in lines]


# walk the field
seen={}
result = go(field,seen)

# print result
print(result)