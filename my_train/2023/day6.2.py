import re
#实际上只有一组数据，忽略空格，把time和distance拼接回去再计算ways
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input6.txt", "r") as f:
    lines=f.read().strip().split("\n")
times=re.findall("\d+",lines[0])                       #提取time和distance并拼接后换为int类型
time=""
for item in times:
    time=time+item
time=int(time)
distances=re.findall("\d+",lines[1])
distance=""
for item in distances:
    distance=distance+item
distance=int(distance)

count=0
for j in range(time):         #计算种数
    v=j
    t=time-j
    d=v*t
    if d>distance:
        count+=1
print(count)