#用机器人去操作机器人去操作数字键盘输入密码，知道数字键盘的密码，找出自己的输入
from itertools import permutations            #导入排列组合工具
def tuple_add(a, b):
    a1, a2 = a
    b1, b2 = b 
    return (a1 + b1, a2 + b2)                 #向量加法，用于计算新位置


def get_delta(a, b):
    a1, a2 = a
    b1, b2 = b 
    return (b1 - a1, b2 - a2)                 #计算两个位置之间的差值，即移动向量


def get_delta_string(delta):
    a, b = delta
    out = ""                                  #根据移动向量生成对应的移动字符串

    if b < 0:
        b = -b
        out += b * "<"                        #左右移动
    else:
        out += b * ">"

    if a < 0:
        a = -a
        out += a * "^"                        #上下移动
    else:
        out += a * "v"                        

    return out


def get_permutations(s):                      #获取字符串的所有排列组合，去重
    return list(set(permutations(s)))


def is_allowed(position, moves):
    for move in moves:
        position = tuple_add(position, m[move])     #根据移动更新位置
        if position == (0, -2):                     #如果位置移动到(0, -2)，则不允许
            return False
    return True
    

def type_code(code, pad, level):
    if level == 3:                                  #递归基准情况，如果层级达到3，返回编码长度
        return len(code)

    length = 0
    i, j = 0, 0
    for char in code:
        delta = get_delta((i, j), pad[char])        #计算移动到下一个字符的向量
        delta_string = get_delta_string(delta)      #将向量转换为移动字符串
        possible_codes = get_permutations(delta_string)  #获取所有可能的移动排列
        possible_length = float("inf")                   #可能长度设为正无穷
        for combination in possible_codes:
            if not is_allowed((i, j), combination):      #检查移动是否允许
                continue
            combination = combination + ("A",)           #添加"A"表示结束
            possible_length = min(possible_length, type_code(combination, pad_directional, level + 1))    # 递归计算编码长度，更新最小可能长度
        length += possible_length                        #累加长度
        i, j = pad[char]                                 #更新当前位置
    return length                                        #返回总长度

with open("C:\\Users\\lxlaptop\\Desktop\\input\\input21.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")

#定义数字键盘和方向键盘的布局
pad_numeric = {"A" : (0, 0), "0" : (0, -1), "3" : (-1, 0), "6" : (-2, 0), "9" : (-3, 0), "2" : (-1, -1), "5" : (-2, -1), "8" : (-3, -1), "1" : (-1, -2), "4" : (-2, -2), "7" : (-3, -2)}
pad_directional = {"A" : (0, 0), "^" : (0, -1), "v" : (1, -1), "<" : (1, -2), ">" : (1, 0)}

#定义移动映射
m = {"^" : (-1, 0), "v" : (1, 0), "<" : (0, -1), ">" : (0, 1)}

result = 0
for code in lines:                                            #计算每行编码的长度并乘以编码前的数字，累加到结果中
    result += type_code(code, pad_numeric, 0) * int(code[:-1])

print(result)