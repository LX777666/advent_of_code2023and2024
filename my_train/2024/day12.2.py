#现在不计算周长了，只需要边长即可，注意避免同一边长多次计算，价格等于面积×边长
def count_area(i, j, plant, field):                                     #先把无法进行下次递归的三种情况进行统计
	if not (0 <= i < len(field) and 0 <= j < len(field[0])):            #离开field区域，则面积不变
		return 0
	if field[i][j] == plant.lower():                                    #已经被探索过，则面积不变
		return 0
	if field[i][j] != plant.lower() and field[i][j] != plant:           #碰到其他植物，则面积不变
		return 0
	field[i][j] = plant.lower()                                         #确认为符合植物，将该区域标记为探索过(通过把字母变为小写来标记)               
	north = count_area(i + 1, j, plant, field)                          #然后向四方进行探索
	south = count_area(i - 1, j, plant, field)
	west = count_area(i, j + 1, plant, field)
	east = count_area(i, j - 1, plant, field)
	return (1 + north + south + west+ east)                             #加的1代表现在所在的区域符合，面积加1

def is_inbounds(i, j):                                                  #定义函数快速判断是否在界域内
	return 0 <= i < len(field) and 0 <= j < len(field[0])		        

def count_perimeter(plant, field):                                      #计数边数
	perimeter=0
	for i in range(len(field)):
		for j in range(len(field[0])):
			if field[i][j]!=plant:                                      #遍历每一个plant，对于非plant格不予考虑直接跳过
				continue
			north=field[i-1][j] if is_inbounds(i-1, j) else "."         #对东南西北以及东南，东北，西南，西北八个方向的元素进行赋值
			east=field[i][j+1] if is_inbounds(i, j+1) else "."          #使用if函数，若在界域内则赋值对应位置元素，否则赋值为"."
			west=field[i][j-1] if is_inbounds(i, j-1) else "."
			south=field[i+1][j] if is_inbounds(i+1, j) else "."
			eastnorth=field[i-1][j+1] if is_inbounds(i-1, j+1) else "."
			westnorth=field[i-1][j-1] if is_inbounds(i-1, j-1) else "."
			eastsouth=field[i+1][j+1] if is_inbounds(i+1, j+1) else "."
			westsouth=field[i+1][j-1] if is_inbounds(i+1, j-1) else "."
			perimeter+=1 if north!=plant else 0                                           #先判断东南西北四个方向，若不为植物，则直接边长+1
			perimeter+=1 if east!=plant else 0
			perimeter+=1 if west!=plant else 0
			perimeter+=1 if south!=plant else 0
			perimeter-=1 if north!=plant and west==plant and westnorth!=plant else 0      #但考虑到有重复叠加同一边长情况，进行另一种判断，减少边长
			perimeter-=1 if west!=plant and south==plant and westsouth!=plant else 0      #这里是按照逆时针方向，对每一个角度是否重复计算边长做出判断和处理
			perimeter-=1 if south!=plant and east==plant and eastsouth!=plant else 0      #如此时北边不为plant于是边长+1，但此时他的西边是plant且西边的北边也不为plant，也会+1
			perimeter-=1 if east!=plant and north==plant and eastnorth!=plant else 0      #于是这两个都会+1，重复了，所以减少1，其他方向同理（也不一定非要按一个逆时针方向来，只要四个方向都考虑了就行）
	return perimeter

def delete_area(plant, field):                                          #判断完成之后，这一个块区域的边长和面积都计算完了，避免重复计算，把整个区域都变成“.”
	for i in range(len(field)):
		for j in range(len(field[0])):
			if field[i][j] == plant:
				field[i][j] = "."
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input8.txt",mode="r",encoding="utf-8") as f:
   f1=f.read().strip().split("\n")
field=[[s for s in line] for line in f1]

price = 0
for i in range(len(field)):
	for j in range(len(field[0])):
		if field[i][j] != ".":
			plant=field[i][j]
			area = count_area(i, j, plant, field)
			perimeter=count_perimeter(plant.lower(), field)            #因为在计算面积之后，会把plant变成小写标记，刚好把这个区域标记完了
			price += area * perimeter                                  #所以这里计算边长是按小写的来计算，刚好避免区块外面的同一种字母对计算边长造成影响
			delete_area(plant.lower(), field)                 
print(price)