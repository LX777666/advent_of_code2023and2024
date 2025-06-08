#从地图起点走到终点，只有一条路径，但现在可以作弊一次，可以翻过墙壁走两步，问多少种作弊方式可以让到达终点的步数减少超过100步
from collections import Counter
import sys


def get_char(char, field):                      #找坐标函数
	for i in range(len(field)):
		for j in range(len(field[0])):
			if field[i][j] == char:
				return (i, j)
			

def number(i, j, nr, field):                    #给路径标上数字，表明到终点的路径和步数
	if field[i][j] == "#":
		return
	if type(field[i][j]) == int:
		return
	field[i][j] = nr                            #非'#'和非数字，即可把该位置标为路径坐标数
	number(i - 1, j, nr + 1, field)             #朝着四个方向，每个方向给的路径坐标数是一样的
	number(i + 1, j, nr + 1, field)
	number(i, j - 1, nr + 1, field)
	number(i, j + 1, nr + 1, field)


def make_next_step(i, j, step, field):          #寻找下一步的坐标，看看四个方向走哪边
	if step == 0:
		return get_char(0, field)
	if field[i - 1][j] == step:
		return (i - 1, j)
	if field[i + 1][j] == step:
			return (i + 1, j)
	if field[i][j - 1] == step:
			return (i, j - 1)
	if field[i][j + 1] == step:
			return (i, j + 1)
	

def get_field(i, j, field):                   #定义函数，用于获取指定位置的字段值
	if 0 <= i < len(field) and 0 <= j < len(field[0]) and type(field[i][j]) == int:
		return field[i][j]
	else:
		return 0                              #若为非int类型或超出范围，返回0


def get_neighbours(i, j):             #找到i，j的四个方位临界点
	result = set()
	result.add((i - 1, j))
	result.add((i + 1, j))
	result.add((i, j - 1))
	result.add((i, j + 1))
	return result


def apply_cheat(i, j, step, field):
	neighbours1 = get_neighbours(i, j)
	neighbours2 = set()
	for a,b in neighbours1:
		neighbours2.update(get_neighbours(a, b))                              #把四个方向的坐标中每一个方向的四个方向坐标列入neighbours2里，update同一坐标不会重复添加
	result = [(a, b, get_field(a, b, field)) for a, b in neighbours2]
	cheats = [(a, b, time - step - 2) for a, b, time in result if time > step + 2]               #若作弊到达的地点的time比按顺序走到的步数大，即说明该作弊成功减少步数了
	return cheats                                                                                #则把节省的步数返回，即time - step - 2


#重新设置递归深度
sys.setrecursionlimit(10000)

with open("C:\\Users\\lxlaptop\\Desktop\\input\\input20.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
    field=[[s for s in line] for line in lines]

start_i, start_j = get_char("S", field)                 #找出起点和终点的坐标位置
end_i, end_j = get_char("E", field)
number(start_i, start_j, 0, field)                      #从起点开始对按顺序的步骤进行标数

# try cheats
all_cheats = []
race_time = field[end_i][end_j]                         #到终点的正常步长

i, j = start_i, start_j
for step in range(race_time):                           #从起点开始，逐步尝试作弊
	i, j = make_next_step(i, j, step, field)            #找到下一步的方向（按数字顺序）
	cheats = apply_cheat(i, j, step, field)             #应用作弊程序
	all_cheats.extend(cheats)                           #将作弊步骤添加到总列表中 

times = [time for _, _, time in all_cheats]             #找出all_cheats里面所有的节省步长
times_counter = Counter(times)                          #将节省的步长，以及节省这么多步长的作弊方法个数变成字典的类型，其中key为节省步长time，value为作弊方法个数

result = 0
for key in times_counter:                               # 计算结果，即时间大于等于100的作弊步骤的总数
	if key >= 100:
		result += times_counter[key]

# print result
print(result)