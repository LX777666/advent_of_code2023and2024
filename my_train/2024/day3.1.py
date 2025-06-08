#在一堆乱码字符串里面查找mul(a,b)再把所有a,b相乘累加起来
import re
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input3.txt",mode="r",encoding="utf-8") as f:
    str1=f.read()
pattern = "mul\(\d+,\d+\)"             #定义mul(a,b)类型数据正则表达式  每个符号(  )前面要加个\
res = re.findall(pattern,str1)         #re.findall()函数，先pattern，再字符串
sum=0
for i in range(len(res)):         
    res2=re.findall("\d+",res[i])     #把每个匹配项mul(a,b)中的a,b提取出来(字符串类型)，转为int类型进行计算
    n=int(res2[0])*int(res2[1])
    sum+=n
print(sum)