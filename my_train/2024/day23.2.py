#找到最大的互联计算机集合，并按字母顺序把计算机名字输出，以逗号隔开
from itertools import combinations


def find_password(d):                                               #定义寻找密码的函数
	for computer in d:                                              #遍历每一个键，即电脑名称
		current = d[computer]                                       #当前键的值   
		intersections = []                                          #有len(current)-1个
		for comp in current:
			if comp == computer:
				continue
			intersections.append(current.intersection(d[comp]))     #计算当前电脑computer与其他电脑的连接交集
		                                                            #把当前电脑computer所在的所有交集以{}形式放入一个列表intersections里
		for n in range(14,3,-1):                                    #从len(current)即14开始排列组合current(current最长14)n最小取到4
			for comb in combinations(current, n):                   #遍历每种组合
				comb_set = set(comb)                                #设置成元组形式
				frequency = 0
				for intersection in intersections:      
					if comb_set.issubset(intersection):             #如果组合是交集的子集，则增加频率计数
						frequency += 1
				if frequency >= n - 1:                              #如果comb_set（n个电脑的组合）满足是intersection的子集的次数大于等于n-1，则满足密码条件，则认为找到了密码
					password = sorted(list(comb))                   #对密码进行排序，返回密码
					return password
	return 0

with open("C:\\Users\\lxlaptop\\Desktop\\input\\input23.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
lan = [line.split("-") for line in lines]


                                                          
d = {}                                                      #初始化字典
for connection in lan:                                      #填充网络
    a, b = connection
    d[a] = d[a].union({b}) if a in d else {a, b}
    d[b] = d[b].union({a}) if b in d else {a, b}
                                                            #寻找密码
password_list = find_password(d)
result = ",".join(password_list)                            #如果找到了密码，则将字符列表转换为逗号分隔的字符串

print(result)