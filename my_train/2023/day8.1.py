import re
#按照指令，不断地走路口，从AAA开始到ZZZ，
with open("C:\\Users\\sage\\Desktop\\train\\input2\\input8.txt", "r") as f:
    items=f.read().strip().split("\n\n")
instructions=items[0]
map=items[1].split("\n")
dict={}        #存入字典，左边键为当前位置，值为列表，包含左右方向的值
for line in map:
    res=re.findall("\w+",line)
    dict[res[0]]=[res[1],res[2]]
now="AAA"
count=0
for i in range(10000000):
    instruction=instructions[i%len(instructions)]   #用%循环使用instructions
    if instruction=="L":
       now=dict[now][0]
    else:
       now=dict[now][1]
    count+=1
    if now=="ZZZ":
        break
print(count)