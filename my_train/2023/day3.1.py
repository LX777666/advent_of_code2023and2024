#找到所有和零件相邻的数字并累加和
#对单行的字符串寻找可能的数字
def get_part_numbers(row):
    """
    Extract all the possible part numbers from a row.
    """
    part_numbers = {}  # 用于存储部分数字及其起始索引
    part_number = ""  # 用于构建部分数字的字符串
    for i, char in enumerate(row):
        try:
            part_number += f"{int(char)}"  # 尝试将字符转换为整数并添加到部分数字字符串中
        except ValueError:                 # 若为数字，则存入，若为符号，直接跳转到except，一开始就是符号则part_number为空不做处理
            if part_number:                # 存入数字后出现符号，则按照起始索引直接把part_number加到part_numbers字典中
                for j in range(len(part_number)):
                    part_numbers[i - j - 1] = int(part_number)  # 将部分数字及其起始索引存入字典
                part_number = ""  # 重置部分数字字符串
    for j in range(len(part_number)):
        part_numbers[i - j - 1] = int(part_number)  # 处理行末尾的部分数字(没有取到字符报错，无法进入except存储)
    return part_numbers

def find_adjacent_part_numbers(x, y, grid):
    """
    Find a distinct set of part numbers adjacent to the supplied (x, y) in the grid.
    """
    v = set()  # 用于存储相邻的部分数字，用元组避免同一数字

    # 遍历下一行
    if y + 1 < len(grid):
        part_numbers = get_part_numbers(grid[y + 1])  # 获取下一行的部分数字
        if x - 1 >= 0 and x - 1 in part_numbers:      # 确认范围
            v.add(part_numbers[x - 1])  # 添加左下方的部分数字
        if x in part_numbers:
            v.add(part_numbers[x])  # 添加正下方的部分数字
        if x + 1 < len(grid) and x + 1 in part_numbers:
            v.add(part_numbers[x + 1])  # 添加右下方的部分数字

    # 遍历当前行
    part_numbers = get_part_numbers(grid[y])  # 获取当前行的部分数字
    if x - 1 >= 0 and x - 1 in part_numbers:
        v.add(part_numbers[x - 1])  # 添加左方的部分数字
    if x in part_numbers:
        v.add(part_numbers[x])  # 添加当前位置的部分数字
    if x + 1 < len(grid) and x + 1 in part_numbers:
        v.add(part_numbers[x + 1])  # 添加右方的部分数字

    # 遍历上一行
    if y - 1 >= 0:
        part_numbers = get_part_numbers(grid[y - 1])  # 获取上一行的部分数字
        if x - 1 >= 0 and x - 1 in part_numbers:
            v.add(part_numbers[x - 1])  # 添加左上方的部分数字
        if x in part_numbers:
            v.add(part_numbers[x])  # 添加正上方的部分数字
        if x + 1 < len(grid) and x + 1 in part_numbers:
            v.add(part_numbers[x + 1])  # 添加右上方的部分数字

    return v

def build_grid():
    grid = []  # 用于存储网格
    with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input3.txt", "r") as f:
        for line in f:
            grid.append(list(line.strip()))  # 读取文件并构建网格
    return grid


s = 0  # 用于存储结果的总和
grid = build_grid()  # 构建网格
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char not in [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            matches = find_adjacent_part_numbers(x, y, grid)  # 查找相邻的部分数字
            s += sum(matches)  # 将相邻部分数字的和加到总和中
print(s)
