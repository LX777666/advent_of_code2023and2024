#有很多个连接，把两个计算机连接起来，若三个计算机两两相连，则定义为一台互联计算机集合，找出有多少个含名称以t开头的计算机的互联计算机集合
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input21a.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
lan = [line.split("-") for line in lines]          #按照连接符号-来分割

d = {}                                             #创建一个空字典，存入每个元素，并把其相连接的其他所有元素作为它的值
for connection in lan:
	a, b = connection                       
	d[a] = d[a].union({b}) if a in d else {b}      #如果键a在d内存在，则对键a元素的值加上b元素，否则把b作为键a的值存入d中
	d[b] = d[b].union({a}) if b in d else {a}      #同上

                                                   #寻找互联计算机集合
triples = set()                                    #创建一个空元组
for a in d:                                        #对每一个键进行处理
	for b in d[a]:                                 #对键a里的每一个值进行处理 
		if b == a:                                 #若键与值相同，不做处理 
			continue
		for c in d[b]:                             #把该值b作为键，对键b的每一个元素进行处理
			if c == b:                             
				continue
			if a in d[c]:                          #若元素a也在b的元素c的值内
				triple = [a, b, c]                 #则说明三个元素abc两两连接，将其编入一个列表，并排序后加入元组triples
				triple.sort()                  
				triples.add(tuple(triple))

                                                
result_list = [(a, b, c) for a, b, c in triples if a[0] == "t" or b[0] == "t" or c[0] == "t"]   #找到包含以t开头的电脑的计算机集合
result = len(result_list)
print(result)