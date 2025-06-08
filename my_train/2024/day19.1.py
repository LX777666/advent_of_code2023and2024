#给出一些拼块，和一堆字符串，判断字符串可否用这些拼块拼出来
import re
def is_possible(pattern, op, d):
	if pattern == "":                  #如果pattern为空，则说明全都能被组合，返回1
		return True
	if pattern in d:                   #如果该pattern在d里面能找到，则直接返回该pattern的可能性
		return d[pattern]
	for towel in op:                   
		if pattern.startswith(towel):  #遍历towel，若pattern以towel开头，将其开头这段截掉，判断后半部分能否被组合 
			if is_possible(pattern[len(towel):], op, d):
				return True
	d[pattern] = False                 #若都不能以其开头，则说明这个pattern不能被组合，将其存入d字典库里面，并返回False
	return False
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input19a.txt",mode="r",encoding="utf-8") as f1:
    lines1=f1.read().strip()
    op=re.findall("\w+",lines1)        #读取所有towel
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input19b.txt",mode="r",encoding="utf-8") as f2:
    lines2=f2.read().strip() 
    patterns=re.findall("\w+",lines2)  #读取所有pattern
result = 0
for pattern in patterns:                   #d是一个字典，存入不同类型pattern以及其组合方式
	result += 1 if is_possible(pattern, op, {}) else 0
print(result)