#定义change函数，按照规则，将列表的数字进行改变，
def change(list):
    n=len(list)
    temp_list=list                                                         #定义一个暂时的列表，将list数据存入其中，然后把list清零，重新进行操作
    list=[]
    for i in range(n):
        if temp_list[i]==0:                                               
            list.append(1)
        elif len(str(temp_list[i]))>=2 and len(str(temp_list[i]))%2==0:    #判断数字是偶数位（长度大于2，取余2为0）
            num_str=str(temp_list[i])                                      #变成字符串更方便计算位数以及切片
            half=len(num_str)//2
            parts=[int(num_str[:half]),int(num_str[half:])]                #对半切
            list.append(parts[0])
            list.append(parts[1])
        else:
            list.append(temp_list[i]*2024)
    return list
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input11.txt",mode="r",encoding="utf-8") as f:
    f1=f.read().split()
list=[int(s) for s in f1]
for n in range(25):
  list=change(list)
print(len(list))