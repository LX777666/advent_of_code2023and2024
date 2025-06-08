from collections import defaultdict
def count_valid_combinations(s, target_lengths):
    n = len(s)
    target_set = set(target_lengths)
    max_target = max(target_lengths) if target_lengths else 0

    # dp[i][j][k] 表示处理到第 i 个字符，当前连续 # 的个数为 j，匹配状态为 k 的组合数量
    dp = defaultdict(int)
    dp[(0, 0, 0)] = 1

    for i in range(1, n + 1):
        current_char = s[i - 1]
        new_dp = defaultdict(int)

        for (pos, consecutive, satisfied), count in dp.items():
            if pos == i - 1:
                if current_char == '?' or current_char == '.':
                    # 变成 .，重置连续 # 的个数
                    new_state = (i, 0, satisfied)
                    new_dp[new_state] += count
                if current_char == '?' or current_char == '#':
                    # 变成 #，增加连续 # 的个数
                    new_consecutive = consecutive + 1
                    new_satisfied = satisfied
                    if new_consecutive in target_set:
                        new_satisfied |= (1 << target_lengths.index(new_consecutive))
                    new_state = (i, new_consecutive, new_satisfied)
                    new_dp[new_state] += count

        dp = new_dp

    # 计算满足所有目标数字的组合数量
    result = 0
    final_satisfied = (1 << len(target_lengths)) - 1
    for (pos, consecutive, satisfied), count in dp.items():
        if satisfied == final_satisfied:
            result += count

    return result

# 示例
s = ".??..??...?##."
target_lengths = [1, 1, 3]
print(f"满足条件的组合数量: {count_valid_combinations(s, target_lengths)}")