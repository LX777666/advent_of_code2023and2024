#在多行数据中，对每行数据进行推导，用该行数据两两之间的差值作为新的一行，并再对新的一行进行同样操作
#直到该行数据为全0，然后在每行的末尾进行反向推导，找到原始行的下一个数据，并累加起来
with open("C:\\Users\\sage\\Desktop\\train\\input2\\input9.txt", "r") as f:
    lines=f.read().strip().split("\n")
def isempty(list):                  #判断该行是否全为0
    for i in range(len(list)):
        if list[i]!=0:
            return 0
    return 1
def diff(line):                     #计算该行的差值行
    temp=[]
    for i in range(len(line)-1):
        diff=line[i+1]-line[i]
        temp.append(diff)
    return temp
def addnext(list):                  #通过处理list，找到下一个数据
   num=0
   for i in range(len(list)):
       line=list[i]
       num+=line[-1]
   return num
def addfirst(list):         #通过处理list找到前一个数据
    num=0
    for i in range(len(list)-1,-1,-1):
        line=list[i]
        num=line[0]-num
    return num
count=0
for line in lines:
    line=line.split(" ")       #处理每一行数据
    line=[int(x) for x in line]
    list=[line]
    while True:
        temp=diff(line)
        list.append(temp)
        if isempty(temp)==1:
            break
        line=temp
    count+=addnext(list)
print(count)