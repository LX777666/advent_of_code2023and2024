#在一个map里有各种符号，同一种符号两两之间会产生反应，在对应镜像的位置产生#，若镜像位置是另一种符号则记录位置，并也算作一个#计入计数，求#个数
import itertools
def change(location,map,path):                               #定义函数，改变map中的元素，将对角的非#元素改为#，并加入path中
    count1=0                                                        
    combinations=list(itertools.combinations(location,2))    #将特殊符号的所有位置进行两两组合，并转换为list
    for combal in combinations:                              #提取每一种组合，对延申的等距对角位置进行判断操作
        new1=[0,0]                                           #两个对角位置的位置信息
        new2=[0,0]
        new1[0]=combal[1][0]-(combal[0][0]-combal[1][0])     #即坐标x，依次类推
        new1[1]=combal[1][1]-(combal[0][1]-combal[1][1])
        new2[0]=combal[0][0]-(combal[1][0]-combal[0][0])
        new2[1]=combal[0][1]-(combal[1][1]-combal[0][1])
        if new1[0]>=0 and new1[0]<len(map) and new1[1]>=0 and new1[1]<len(map[0]):   #判断该位置是否在map内
            if map[new1[0]][new1[1]]=="." :                                          #如果该位置元素为. 字节转换为#并记录位置到path
                 map[new1[0]][new1[1]]="#"
                 path.append(new1)
            elif  [new1[0],new1[1]] not in path:             #对非.字符则判断是否在path内，若已经在里面则不做处理，若不在则count1加1并存入path
                path.append(new1)
                count1+=1
        if new2[0]>=0 and new2[0]<len(map) and new2[1]>=0 and new2[1]<len(map[0]):
            if map[new2[0]][new2[1]]=="." :
                 map[new2[0]][new2[1]]="#"
                 path.append(new2)
            elif  [new2[0],new2[1]] not in path:
                path.append(new2)
                count1+=1
    return count1                                            #对非.的字符位置计入1，并计算所有值后返回给函数外
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
path=[]
for item in elements:                     #查找每种元素的所有位置
    address=[]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]==item:
                address.append([i,j])
    count+=change(address,map,path)            
for i in range(len(map)):                #再把所有的#计数，加起来
    for j in range(len(map[0])):
        if map[i][j]=="#":
            count+=1                       
print(count)
