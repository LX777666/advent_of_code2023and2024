#现在字符串中有一些数字的英文表示，将这些英文也作为数字处理，然后重新找出第一个数字和最后一个数字进行拼接，和累加
from copy import deepcopy 
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input1.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
#替换单词的字典
replacement_dict = {'one': '1','two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9','zero': '0'}
#找出第一个数字
def first_digit_part2(line):
    for ind, char in enumerate(line):
        if char in '0123456789':
            return char
        else:
            for number in replacement_dict:
                if line[ind:].startswith(number):      #如果从该标记之后的字符串以number开头，则将该number替换成数字
                    return replacement_dict[number]
def last_digit_part2(line):
    line = "".join(reversed(line))                     #将改字符串逆序 
    for ind, char in enumerate(line):
        if char in '0123456789':
            return char
        else:
            for number in replacement_dict:          
                if line[ind:].startswith(number[::-1]): #以number的逆序为开头，即从字符串的末尾开始找到的第一个number
                    return replacement_dict[number]
result= 0
for line in lines:
    line = line.strip()
    chars = first_digit_part2(line) + last_digit_part2(line)
    result+= int(chars)
print(result)