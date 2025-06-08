#判断每个字符串的拼接方式有多少种，并累加起来
import re
def combinations(pattern, op, d):
	if pattern == "":
		return 1
	if pattern in d:
		return d[pattern]
	possiblilities = 0
	for towel in op:
		if pattern.startswith(towel):
			possiblilities += combinations(pattern[len(towel):], op, d)	
	d[pattern] = possiblilities
	return possiblilities
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input19a.txt",mode="r",encoding="utf-8") as f1:
    lines1=f1.read().strip()
    op=re.findall("\w+",lines1)
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input19b.txt",mode="r",encoding="utf-8") as f2:
    lines2=f2.read().strip()
    patterns=re.findall("\w+",lines2)
result = 0
for pattern in patterns:
	result +=combinations(pattern, op, {})
print(result)