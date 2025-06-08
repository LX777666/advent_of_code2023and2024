import re
#现在所有以A结尾的都是起点，所有起点同时进行，直到所有位置都以Z结尾才停止
def pgcd(a, b):        #计算两个数的最大公约数
    while b != 0:
        a, b = b, a % b
    return a
def ppcm(a, b):        #计算两个数的最小公倍数
    return a * b // pgcd(a, b)
def ppcm_liste(nombres): #计算一个数字列表的最小公倍数
    resultat = nombres[0]
    for nombre in nombres[1:]:
        resultat = ppcm(resultat, nombre)
    return resultat
with open("C:\\Users\\sage\\Desktop\\train\\input2\\input8.txt", "r") as f:
    items=f.read().strip().split("\n\n")
instructions=items[0]
map=items[1].split("\n")
dict={}
for line in map:
    res=re.findall("\w+",line)
    dict[res[0]]=[res[1],res[2]]

keys=dict.keys()        #找到所有的A结尾的键，和所有Z结尾的键
Akeys=[]
Zkeys=[]
time=[]
for key in keys:
    if key.endswith("A"):
       Akeys.append(key)
    if key.endswith("Z"):
       Zkeys.append(key)
for j in range(len(Akeys)):    #对每个起点进行处理，找到每个起点找到Z结尾的位置的时间
  count=0
  for i in range(10000000):
    instruction=instructions[i%len(instructions)]   #用%循环使用instructions
    if instruction=="L":
       Akeys[j]=dict[Akeys[j]][0]
    else:
       Akeys[j]=dict[Akeys[j]][1]
    count+=1
    if Akeys[j] in Zkeys:
        time.append(count)
        break
print(ppcm_liste(time))      #所有起点到达Z结尾终点的时间的最小公倍数，即为要寻找的时间