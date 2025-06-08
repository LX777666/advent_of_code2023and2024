#一堆图纸，先判断是钥匙还是锁，然后对其进行高度代指，再根据高度，判断锁和钥匙是否会重合，从而筛除冗余选项，更容易找出正确的钥匙
def islock(item):                                     #判断是否为锁（是否是顶部一整行#）
    lock=0
    key=0
    for j in range(5):
        if item[0][j]=="#":
            lock+=1
        if item[6][j]=="#":                           #判断是否为钥匙（是否是以底部一整行#）  
            key+=1    
    if lock==5:
        return 1
    if key==5:
        return 0 
def lock_to_heigts(item):                             #把lock转换为高度表示  
    heigt=[0,0,0,0,0]
    for i in range(7):
        for j in range(5):
           if item[i][j]=="#":
               heigt[j]=i
    return heigt
def key_to_heigts(item):                              #把key转换为高度表示
    heigt=[6,6,6,6,6]
    for i in range(7):
        for j in range(5):
            if item[i][j]==".":
                heigt[j]=6-i-1
    return heigt
def isoverlap(key,lock):                              #判断高度是否重合（即钥匙与锁是否会匹配）
    flag=0
    for i in range(5):
        if key[i]+lock[i]>=6:
            flag=1
    return flag
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input25.txt", mode="r",encoding="utf-8") as f:
    items=f.read().strip().split("\n\n")              #双\n，把每个图案分隔开来
lock=[]                                               #定义lock和key列表，用于分别存储key和lock
key=[]
for item in items:                                    #对每个图案进行处理
    item=item.split("\n")                             #按分行符划分为列表形式
    if islock(item):                                  #判断是否为锁，并以此分别存入对应列表内
        lock.append(item)
    else:
        key.append(item)

heigts_key=[]                                         #定义锁和钥匙的高度列表
heigts_lock=[]
for item in key:                                      #遍历key中的每一个元素，将其转换为高度表示并存入heigts_key
   heigt=key_to_heigts(item)                         
   heigts_key.append(heigt)
for item in lock:                                     #遍历lock中的每一个元素，将其转换为高度表示并存入heigts_lock
   heigt=lock_to_heigts(item)
   heigts_lock.append(heigt)
fit=0                                                 #初始化符合的个数fit
for i in range(len(heigts_key)):
    for j in range(len(heigts_lock)):
         if isoverlap(heigts_key[i],heigts_lock[j])==0:    #若判断重叠结果为0，即未重叠，符合要求，fit+1
             fit+=1
print(fit)