import re    
#现在不算分数，每个卡牌中奖个数n后，都按照卡牌号顺序往后增加n个卡牌，问一共计算了多少张卡牌
def count_copy(key,keys,sum):             #定义函数，计算个数并把复制的卡牌加入keys列表中
    n=keys.count(key)                     #计算key的个数
    sum+=n
    keys=keys+ count_list_dict[key]*n     #把key对应的要添加的号码添加n次到keys里
    keys=[x for x in keys if x != key]    #删除所有的key
    keys.sort()                           #重新排序
    return keys,sum
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input4.txt", "r") as f:
    lines=f.read().strip().split("\n")
sum=0
dict={}                                   #定义字典，卡牌号及对应的中奖号码和自己的号码
num_count_dict={}                         #定义字典，每个卡牌号对应的中奖个数
count_list_dict={}                        #定义字典，每个卡牌号对应的要添加的卡牌号码
for line in lines:
    line=re.findall("\d+",line)
    key=int(line[0])
    dict[key]=line[1:]
keys=list(dict.keys())                    #单独找出keys，只处理key就好，不用处理其他号码 
for key in keys:                          #计算num_count_dict
    win_number=dict[key][:10]
    my_number=dict[key][10:]
    count=0
    for win in win_number:
        if win in my_number:
            count+=1
    num_count_dict[key]=count
for key in keys:                         #计算count_list_dict
   count=num_count_dict[key]
   templist=[]
   for i in range(count):
       templist.append(i+key+1)
   count_list_dict[key]=templist
for key in keys:
   keys,sum=count_copy(key,keys,sum)
print(sum)