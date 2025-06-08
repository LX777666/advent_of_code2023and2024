import re
#给出机器人的位置和移动速度方向，在一个可以循环穿透的地图里（走到上方地图外会从下方出来），计算n秒后
#四个象限的机器人有多少个并乘起来作为安全系数
def move(p,v,map):
    i,j=int(p[0]),int(p[1])
    vx,vy=int(v[0]),int(v[1])
    n=100
    dx=(i+n*vx)%101
    dy=(j+n*vy)%103
    if map[dy][dx]==".":
       map[dy][dx]=1
    else:
       map[dy][dx]+=1
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input14.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
map=[]
for i in range(103):
    row = []
    for j in range(101):
        row.append('.')
    map.append(row)
for line in lines:
    item=re.findall("-?\d+",line)
    p=item[:2]
    v=item[2:]
    move(p,v,map)
for i in range(len(map)):
    for j in range(len(map[0])):
        if i==51 or j==50:
            map[i][j]="."
p1=0
p2=0
p3=0
p4=0
for i in range(len(map)):
    for j in range(len(map[0])):
       if map[i][j]!=".":
           if i <51 and j <50:
               p1+=map[i][j]
           elif i<51 and j>50:
               p2+=map[i][j]
           elif i>51 and j<50:
               p3+=map[i][j]
           else :
               p4+=map[i][j]
num=p1*p2*p3*p4
print(num)