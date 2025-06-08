#现在同一个符号会产生更多的反应，并不局限于镜像对角处一个位置，而是会延长在这条线上反复出现直到离开map，并且符号自身位置也算入#，计算所有#个数
import itertools
def change(location,map):
    combinations=list(itertools.combinations(location,2))
    for combal in combinations:
        map[combal[0][0]][combal[0][1]]="#"                     #将该组合所有位置元素换为#
        map[combal[1][0]][combal[1][1]]="#"
        new1=[0,0]                                              #定义新的镜像位置
        new2=[0,0]
        for i in range(1,max(len(map),len(map[0]))):            #循环，不停向外延申产生位置，直到位置离开map
          new1[0]=combal[1][0]-(combal[0][0]-combal[1][0])*i    
          new1[1]=combal[1][1]-(combal[0][1]-combal[1][1])*i
          if new1[0]>=0 and new1[0]<len(map) and new1[1]>=0 and new1[1]<len(map[0]):
            if map[new1[0]][new1[1]]=="." :
                 map[new1[0]][new1[1]]="#"
            elif map[new1[0]][new1[1]]=="#":                    #若该位置已经是#则跳过，continue
                 continue
          else:
              break
        for i in range(1,max(len(map),len(map[0]))):
          new2[0]=combal[0][0]-(combal[1][0]-combal[0][0])*i
          new2[1]=combal[0][1]-(combal[1][1]-combal[0][1])*i
          if new2[0]>=0 and new2[0]<len(map) and new2[1]>=0 and new2[1]<len(map[0]):
            if map[new2[0]][new2[1]]=="." :
                 map[new2[0]][new2[1]]="#"
            elif map[new2[0]][new2[1]]=="#" :
                 continue
          else:
              break
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input8.txt",mode="r",encoding="utf-8") as f:
    f1=f.read()
    lines=f1.strip().split("\n")
    map=[list(line) for line in lines]    #生成地图map
elements=set()
for i in range(len(map)):                 #找到map中不同的元素有哪些
    elements=elements.union(map[i])
elements=list(elements)                   #set类型转换为list类型
elements.remove(".")                      #去除掉"."
count=0
for item in elements:
    address=[]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]==item:
                address.append([i,j])
    change(address,map)            
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j]=="#":
            count+=1
print(count)
