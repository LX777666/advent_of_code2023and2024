#现在将没有#的行列扩展为原来的1000000倍
#先将map进行扩展，再计算所有星系间的距离之和
from copy import deepcopy
from itertools import combinations
def expand(map):
    n=999999                          #每次需要增加的行列数
    temp_map=deepcopy(map)            #复制一个map然后用来方便遍历i，j
    new_row=["." for x in range(len(map[0]))]  #要插入的一整行"."
    count=-n                          #初始化count为-1，因为一开始默认flag=1，会多加一个count
    flag=1
    for i in range(len(temp_map)):
        if flag==1:                   #如果上一行有空行，则count加1，方便后续插入找位置
            count+=n
        flag=1                        #再把flag初始化回来，方便判断当前行或列是否为空
        for j in range(len(temp_map[0])):
            if temp_map[i][j]=="#":   #遍历每一个点，只要有一个星系#，则判断为非空，停止遍历
                flag=0
                break
        if flag:                      #如果有空行，则在当前i的基础上加上count，即需要插入的位置
           i+=count                   #插入行
           map = map[:i] + [new_row]*n + map[i:]
    count=-n                          #同上面的行，处理列
    flag=1
    temp_map=deepcopy(map)
    for i in range(len(temp_map[0])): #遍历每一列
        if flag==1:
            count+=n
        flag=1
        for j in range(len(temp_map)):
            if temp_map[j][i]=="#":
                flag=0
                break
        if flag:
            i+=count              #插入一列，区分上面插入行
            for x in range(len(temp_map)):
              map[x] = map[x][:i] + ["."]*n + map[x][i:]
    return map
def step(comb):                   #定义函数，计算每种comb里两个坐标之间的距离
    x=abs(comb[0][0]-comb[1][0])
    y=abs(comb[0][1]-comb[1][1])
    step=x+y
    return step
with open("C:\\Users\\sage\\Desktop\\train\\input2\\input11.txt", "r") as f:
    lines=f.read().strip().split("\n")
    map=[[x for x in line] for line in lines]

map=expand(map)
address=[]                       #找到所有星系的坐标
for i in range(len(map)):
    for j in range(len(map[0])):
         if map[i][j]=="#":
             address.append([i,j])

                                #找到所有可能的组合
combs = list(combinations(address, 2))
distance=0                      #初始化距离
for comb in combs:
    distance+=step(comb)
print(distance)