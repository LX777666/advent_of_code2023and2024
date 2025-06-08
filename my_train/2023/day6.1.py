import re
#玩具船，按住可以加速，松手就会开始跑，在固定时间内，判断有几种按的时长，可以让最终跑的距离突破记录，把每列的种数乘起来
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input6.txt", "r") as f:
    lines=f.read().strip().split("\n")
time=re.findall("\d+",lines[0])                       #提取time和distance并换位int类型
time=[int(x) for x in time]
distance=re.findall("\d+",lines[1])
distance=[int(x) for x in distance]
sum=1
for i in range(4):
    count=0
    for j in range(time[i]):         #计算每列的种数
        v=j
        t=time[i]-j
        d=v*t
        if d>distance[i]:
            count+=1
    if count!=0:
       sum*=count
print(sum)