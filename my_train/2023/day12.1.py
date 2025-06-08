import re
import re
from itertools import product

def generate_all_strings(s):
    # 找到所有 '?' 的位置
    question_indices = [i for i, char in enumerate(s) if char == '?']
    n = len(question_indices)

    # 生成所有可能的替换组合（'.' 或 '#'）
    replacements = product(['.', '#'], repeat=n)

    # 替换 '?' 并生成所有可能的字符串
    all_strings = []
    for replacement in replacements:
        temp = list(s)
        for idx, char in zip(question_indices, replacement):
            temp[idx] = char
        all_strings.append(''.join(temp))
    return all_strings
def count_symbol(str):
    # 使用正则表达式找到所有连续的符号
    symbol="#"
    pattern = f'({re.escape(symbol)}+)'
    matches = re.findall(pattern, str)
    # 计算每个匹配的长度
    counts = [len(match) for match in matches]
    return counts

def ismatch(str,list):
    num_str=count_symbol(str)
    if num_str==list:
        return 1
    else:
        return 0
with open("C:\\Users\\sage\\Desktop\\train\\input2\\inputa.txt", "r") as f:
    lines=f.read().strip().split("\n")
count=0
for line in lines:
    res=line.split(" ")
    num=res[1].split(",")
    num=[int(x) for x in num]
    str=res[0]
    str=str+("?"+str)*4
    all_strings=generate_all_strings(str)
    for string in all_strings:
       count+=ismatch(string,num)
print(count)