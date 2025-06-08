#前面相同，后面规则不同
def count_num(list,index):
    count=0
    for item in list[index:]:
        if item==".":
            count+=1
        else:
            break
    return count   
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
elements=[j for j in range(i+1)]
for i in range(len(elements)-1,-1,-1):
   n=temp_list.count(i)
   m=temp_list.index(i)
   for j in range(m):
       if temp_list[j]==".":
           t=count_num(temp_list,j)
           if t>=n:
               for i in range(n):
                  temp=temp_list[j+i]
                  temp_list[j+i]=temp_list[m+i]
                  temp_list[m+i]="."             
print(temp_list)
sum=0
for i in range(len(temp_list)):     
     if temp_list[i]!=".":                        
       sum+=i*int(temp_list[i])
print(sum)
