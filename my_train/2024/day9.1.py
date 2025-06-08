#一串代码，每两个数字代表存储ID号的个数和自由空间，即202441代表（2个0，0个“.”，2个1，4个“.”，4个2，1个“.”），然后再根据“.”按照某种规则排序
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input9.txt",mode="r",encoding="utf-8") as f:
    f1=f.read().replace("\n","")
num_list=[int(s) for s in f1]                                           #将f1中的每个字符的int类型放入列表中
temp_list=[]
j=0                                               
for i in range(len(num_list)//2+1):                                     #ID号
  if j <len(num_list)-1:                                                #找对应的值，表示循环的次数
    for m in range(num_list[j]):                                        #把ID号存入temp_list，重复j位置的值的次数
            temp_list.append(i)
    for n in range(num_list[j+1]):                                      #存入j+1位置的值的数量个.
            temp_list.append(".")
  j+=2
for m in range(num_list[-1]):
    temp_list.append(i)
for i in range(len(temp_list)):
     if temp_list[i]==".":
          for j in range(len(temp_list)-1,-1,-1):
               if temp_list[j]!=".":
                    if j >i:
                        temp=temp_list[i]
                        temp_list[i]=temp_list[j]
                        temp_list[j]=temp
                        break
s=temp_list.index(".")
temp_list=temp_list[:s]
sum=0
for i in range(len(temp_list)):                             
     sum+=i*int(temp_list[i])
print(sum)
