#除了+和*以外，再加入一个||符号，该符号可让两个数字拼接
import re
import itertools
def calculate(elements):
    # 从左到右计算
    result = int(elements[0])                      #结果里面先加入第一个数
    for i in range(1, len(elements), 2):           #从第一个数开始取，每隔两个数取一次
        operator=elements[i]                       #取出一个运算符
        next_number=int(elements[i + 1])           #取出一个数字
        if operator=='+':
            result+=next_number
        elif operator=='*':
            result*=next_number
        elif operator=="||":
            result=int(str(result)+str(next_number))
    return result
def istrue(sum,numbers):
    # 生成所有可能的运算符 '+' 和 '*' 组合
    operators=['+','*',"||"]
    num_operators=len(numbers)-1
    all_ops_combinations=itertools.product(operators, repeat=num_operators)
    
    # 对于每种组合，插入运算符生成表达式
    flag=0
    for ops in all_ops_combinations:
        expression=[]
        for num, op in zip(numbers,ops):  #将数字和运算符按顺序填入expression字符串
            expression.append(str(num))
            expression.append(op)
        expression.append(numbers[-1])    #填入最后一个数字
        if sum==calculate(expression):    #判断计算值是否等于sum
            flag=1
    return flag,sum

        
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input7.txt", mode="r", encoding="utf-8") as f:
     f1=f.read()                               #读取文件f
     f2=f1.strip().split("\n")                 #把他变成一个列表，每行都是列表的一个元素
count=0
for line in f2:                                #对每一行单独处理，即列表的每一个元素
     pattern="\d+"                             #查找数字类型数据
     num=re.findall(pattern,line)
     for i in range(len(num)):
          num[i]=int(num[i])                   #把数字存入列表num中
     sum=num.pop(0)                            #提取出最前面的总和数字，方便后续对比验证
     flag,sum=istrue(sum,num)
     if flag==1:
         count+=sum
print(count)

     
