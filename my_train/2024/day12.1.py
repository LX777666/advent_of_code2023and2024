#花园中有各种植物，对每种相同植物组成的块进行围栏，计算该块中的植物的面积和围栏的周长，价格等于面积×周长
def count(i, j, plant, field):                                     #先把无法进行下次递归的三种情况进行统计
	if not (0 <= i < len(field) and 0 <= j < len(field[0])):       #离开field区域，则面积不变，周长加1
		return (0, 1)
	if field[i][j] == plant.lower():                               #已经被探索过，则面积周长都不变
		return (0, 0)
	if field[i][j] != plant.lower() and field[i][j] != plant:      #碰到其他植物，则面积不变，周长加1
		return (0, 1)
	field[i][j] = plant.lower()                                    #确认为符合植物，将该区域标记为探索过(通过把字母变为小写来标记)               
	north = count(i + 1, j, plant, field)                          #然后向四方进行探索
	south = count(i - 1, j, plant, field)                          #进行递归函数都可以仿照
	west = count(i, j + 1, plant, field)
	east = count(i, j - 1, plant, field)
	return (1 + north[0] + south[0] + west[0] + east[0],           #加的1代表现在所在的区域符合，面积加1
		 north[1] + south[1] + west[1] + east[1])


with open("C:\\Users\\lxlaptop\\Desktop\\input\\input12.txt",mode="r",encoding="utf-8") as f:
   f1=f.read().strip().split("\n")
field=[[s for s in line] for line in f1]

price = 0
for i in range(len(field)):
	for j in range(len(field[0])):
		if field[i][j] != ".":
			area, perimeter = count(i, j, field[i][j], field)
			price += area * perimeter
print(price)