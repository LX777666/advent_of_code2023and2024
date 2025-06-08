#按照要求对secret进行处理，并迭代2000次后，将所有secret加起来
def calculate_round(secret):                             #对secret进行处理
	secret = ((secret * 64) ^ secret) % 16777216         #乘以64再混合、修剪
	secret = ((secret // 32) ^ secret) % 16777216        #整除32再混合、修剪
	secret = ((secret * 2048) ^ secret) % 16777216       #乘以2048再混合、修剪
	return secret


def secret_number(secret, rounds):               #产生secret number 的函数，输入为secret和迭代次数
	for _ in range(rounds):
		secret = calculate_round(secret)
	return secret

with open("C:\\Users\\lxlaptop\\Desktop\\input\\input22.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
secrets = [int(line) for line in lines]

result = 0
for secret in secrets:
	result += secret_number(secret, 2000)

print(result)