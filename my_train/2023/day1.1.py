#从文件中读取n行信息，每行字符串中包含数字，把字符串的第一个数字和最后一个数字拼接起来组成一个数，然后累加起来为结果
import re
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input1.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
result=0
for line in lines:
    res=re.findall("\d",line)           #找出字符串中的所有数字，单个数字，不需要\d+
    if res!=[]:
        num=int(res[0]+res[-1])         #拼接数字
        result+=num
print(result)