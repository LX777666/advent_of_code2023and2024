#这堆乱码里面有don't()和do()函数仍然起作用，don't()后面的mul()不起作用，do()后面的才起作用,开头的字符串默认起作用。
import re  
pattern = re.compile(r'(?<=don\'t\().+?(?=do\()', re.DOTALL)    # 定义正则表达式模式(don't()开头do()结尾的片段) re.compile()的pattern这里的括号()只在前面加一个\就行？
with open('C:\\Users\\lxlaptop\\Desktop\\input\\input3.txt', 'r', encoding='utf-8') as f:   # 读取文本文件
    str1 = f.read()
matches = pattern.findall(str1)  # 查找所有符合条件的片段,改成了
for match in matches:             # 从字符串中删除所有匹配的片段
   str1= str1.replace(match,"+")
pattern1 = "mul\(\d+,\d+\)"
res = re.findall(pattern1,str1)   #找到所有mul(a,b) 以字符串的形式存入一个列表res   
sum=0             
for i in range(len(res)):        
    res2=re.findall("\d+",res[i])  #把每个匹配项mul(a,b)中的a,b提取出来(字符串类型)，转为int类型进行计算
    n=int(res2[0])*int(res2[1])
    sum+=n
print(sum)