#目标XY增加10000000，A，B按钮的次数不确定了(更多，不止100以内)
import re
def get_a(A, B, prize, b):       #在已知b（按钮B的次数）的情况下找a（按钮A的次数）
	px, py = prize
	ax, ay = A
	bx, by = B
	numerator = px - b * bx
	denominator = ax
	return numerator / denominator

def get_b(A, B, prize):         
	px, py = prize
	ax, ay = A
	bx, by = B
	numerator = px * ay - py * ax              #克拉默法则解线性方程组求a，b，  a*ax + b*bx = px
	denominator = -by * ax + bx * ay           #                              a*ay + b*by = py
	return numerator / denominator


def get_tokens(A, B, prize):
	b = get_b(A, B, prize)
	a = get_a(A, B, prize, b)
	if a == int(a) and b == int(b):
		return int(a * 3 + b)
	else:
		return 0 
def intres(res):
	res[0]=int(res[0])
	res[1]=int(res[1])
	return res
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input13.txt",mode="r",encoding="utf-8") as f:
    f1=f.read().split("\n")
    n=f1.count("")
for i in range(n):
    f1.remove("")
price=0
for i in range(0,len(f1),3):
    res1 = re.findall("\d+",f1[i])
    res1=intres(res1)
    res2 = re.findall("\d+",f1[i+1])
    res2=intres(res2)
    res3 = re.findall("\d+",f1[i+2])
    res3=intres(res3)
    res3[0]=10000000000000+res3[0]
    res3[1]=10000000000000+res3[1]
    price+=get_tokens(res1, res2, res3)
print(price)