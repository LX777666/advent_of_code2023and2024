import re
#中奖卡牌，每一行一个卡片，有中奖号码和自己的号码，未中奖为0，中奖后初始为1，自己的号码中每有一个中奖号码，分数翻倍，问所有卡牌的分数总和
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input4.txt", "r") as f:
    lines=f.read().strip().split("\n")
sum=0
for line in lines:
    line=line.split(":")
    row=line[1]
    res=re.findall("\d+",row)
    win_number=res[:10]                    #分出中奖号码和自己的号码
    my_number=res[10:]
    result=0                               #初始化分数
    flag=0                                 #标记是否中奖
    for win in win_number:
        if win in my_number:
            if flag:
              result*=2
            else:
              result=1                     #重新定义result，并更改标记
              flag=1
    sum+=result
print(sum)  