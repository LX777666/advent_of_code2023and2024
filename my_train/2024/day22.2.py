#现在将每一步的处理后的值的个位进行处理，根据每一次处理后的个位的变化作为一个码，每连续四个码作为一个变化序列
#将变化序列的末尾对应的变化的个位值作为交易的成交额，找到一个变化序列，把每一个secret变化出现该变化序列时的值加起来，使其最大
def calculate_round(secret):                             #对secret进行处理
	secret = ((secret * 64) ^ secret) % 16777216         #乘以64再混合、修剪
	secret = ((secret // 32) ^ secret) % 16777216        #整除32再混合、修剪
	secret = ((secret * 2048) ^ secret) % 16777216       #乘以2048再混合、修剪
	return secret


def generate_sequences(secret, differences, bananas):    #产生片段  
	secrets = []                                         #初始化secrets,再先把初始的secret加入
	secrets.append(secret)
	bananas.append(int(str(secret)[-1]))                 #在bananas里加入产生的secret的末尾数

	for i in range(2000):                                #循环两千次
		secret = calculate_round(secret)                 #先对secret进行处理产生新的secret，然后跟上面一样对secret和bananas进行处理
		secrets.append(secret)
		bananas.append(int(str(secret)[-1]))
		differences.append(bananas[i] - bananas[i - 1])  #最后计算bananas中的变化值，存入differences中


def put(seller_nr, change, banana, changes):             #将某个seller_nr的banana值与一个change元组关联起来，并存储在changes字典中。  
	if change in changes:                                #如果change已经存在于changes字典中，它将只在相应的seller_nr位置更新banana值
		if changes[change][seller_nr] == None:
			changes[change][seller_nr] = banana
	else:
		l = len(sellers) * [None]                        #产生sellers长度的l列表，l列表的第seller_nr个值为该change片段在第seller_nr个seller时产生的banana值
		l[seller_nr] = banana                            #把该l列表作为字典changes的key：change的对应value值
		changes[change] = l 


def generate_changes(seller_nr, differences, bananas, changes):  #遍历differences列表，提取连续的四个差异值作为change元组，并获取对应的banana值
	for i in range(len(differences) - 4):
		change = tuple(differences[i:i + 4])
		banana = bananas[i + 3] 
		put(seller_nr, change, banana, changes)                  #调用put函数将这些值存储在changes字典中


# get input
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input22.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
sellers = [int(line) for line in lines]

changes = {}
for i in range(len(sellers)):                          #计算生成changes和bananas片段
	differences = []
	bananas = []
	secret = sellers[i]
	generate_sequences(secret, differences, bananas)
	generate_changes(i, differences, bananas, changes)

result = 0
for prices in changes.values():
	prices = [x for x in prices if x != None]
	result = max(result, sum(prices))

print(result)