#现在想增加一个障碍物，让守卫在地图里面陷入循环，问有多少种增加障碍物的方法
import os
import sys
sys.setrecursionlimit(10**6)
def isloop(row, col, x, y, map):           # 输入障碍物的位置row，col，以及起点的位置x，y，还有地图矩阵
    temp_map = [list(row) for row in map]  # 使用temp地图以便之后恢复，不影响原来的地图
    temp_map[row][col] = "O"               # 添加障碍物
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}   #设置方向的下一次移动变化
    opposite_directions = {'>': 'v', '^': '>', 'v': '<', '<': '^'}        #设置遇到障碍物之后方向的变化
    path = []  # 存储路径，包括位置和方向

    while True:
        current_direction = temp_map[x][y]                                #起点的方向
        if current_direction not in directions:
            return 0
        idx, idy = x + directions[current_direction][0], y + directions[current_direction][1]  #idx,idy是下一步预期的位置

        # 检查是否超出地图边界
        if idx<0 or idx>=len(temp_map) or idy<0 or idy>=len(temp_map[0]):
            return 0

        # 检查是否形成循环
        if (x, y, temp_map[x][y]) in path:
            return 1

        # 预期位置遇到障碍物，改变方向
        if temp_map[idx][idy] =="#"or temp_map[idx][idy] =="O":
            path.append((x, y, temp_map[x][y]))  # 添加当前位置到路径
            new_direction=opposite_directions[current_direction]   
            temp_map[x][y]=new_direction    # 把位置方向换成新的方向
            idx, idy=x, y                   # 继续在当前位置尝试新的方向
                                            # 没有障碍物，移动到下一个位置
        else:
            temp_map[idx][idy]=current_direction # 若没有障碍物，正常前进，把当前位置方向传递给预期位置
            path.append((x, y, temp_map[x][y]))  # 添加到路径
            x, y = idx, idy  # 更新当前位置
# 读取地图和初始化
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input6.txt", mode="r", encoding="utf-8") as f:
    str_map = f.read()
lines=str_map.strip().split("\n")
map=[list(line) for line in lines]  # 生成地图矩阵

# 查找初始位置
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] =="^":
            x=row
            y=col
            break

# 计算使人物陷入循环的位置数量
count=0
for row in range(len(map)):
    for col in range(len(map[0])):
      if x==row and y==col:
          continue  
      elif map[row][col]=="#":
          continue
      else:
        flag=isloop(row, col, x, y, map)
        count+=flag

print(count)
