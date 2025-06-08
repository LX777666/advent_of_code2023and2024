#在一个地图上爬山，从0到9，每次只能爬一层，方向为上下左右（不能对角），爬到9即记一次数，不算重复爬同一个9的次数，计算有多少个登顶路径（从某个0到某个9）
from copy import deepcopy
def rec(i,j,map,step):                                                  #定义一个递归函数，包括搜索的起点坐标，map以及应该的高度
	if not(0<=i and i<len(map) and 0<=j and j<len(map[0])):
		return 0
	if map[i][j]!=step:
		return 0
	if map[i][j]==9:                                                     #防止重复搜索该终点，将其修改为0
		map[i][j]=0
		return 1
	result=0                                                             #初始化，注意，递归不会将该result覆盖，而是在另一个递归里面初始
	result+=rec(i+1, j, map, step + 1)
	result+=rec(i-1, j, map, step + 1)
	result+=rec(i, j+1, map, step + 1)
	result+=rec(i, j-1, map, step + 1)
	return result

with open("C:\\Users\\lxlaptop\\Desktop\\input\\input10.txt",mode="r",encoding="utf-8") as f:
    f1=f.read().strip().split("\n")
map=[[int(x) for x in list(line)] for line in f1]                       #将map的每个元素变为int，并把map变为列表

result=0
for i in range(len(map)):
	for j in range(len(map[0])):
		if map[i][j]==0:
			map2=deepcopy(map)                                          #先将map深度复制一遍
			result+=rec(i,j,map,0)
			map=map2
print(result)