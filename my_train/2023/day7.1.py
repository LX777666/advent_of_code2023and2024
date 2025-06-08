import re
#骆驼牌，计算每组牌的大小，并把所携带的值与对应大小排序号相乘，进行累加和
def card_type(card):   #计算判断card的类型，并返回对应的等级
   list_n=[]          #计算card内每种字符的个数分配，如32T3K的分配为[2,1,1,1]
   while card:         #直到card为空
      c=card[0]
      n=card.count(c)  #根据字符的个数来计算list_n
      list_n.append(n)
      for i in range(n):
         card=card.replace(c,"")  #删除所有的c
   if list_n.count(5)==1:       #根据list_n的不同分配来定义type和等级值 
     return 7 
   if list_n.count(4)==1:
     return 6
   if list_n.count(3)==1:       #有一种情况都有3，进行区分 
     if 2 in list_n:
          return 5
     else:
          return 4
   if  list_n.count(2)==2:
     return 3
   if  list_n.count(2)==1 and list_n.count(1)==3:
     return 2
   if list_n.count(1)==5:
     return 1
def get_card_value(c):  #将卡牌内字符按照对应值进行转换
  if c == "J":
    return 11
  elif c == "Q":
    return 12
  elif c == "K":
    return 13
  elif c == "A":
   return 14
  elif c=="T":
     return 10
  else:
   return int(c) # 假设其他牌是数字牌
def  compare_card(card1,card2):                    #比较两张卡牌的大小，若card1大于card2则返回1
     if card_type(card1)>card_type(card2):
        return 1
     elif card_type(card1)==card_type(card2):      #若type相等，则按照首字符的大小进行进一步比较
        for i in range(len(card1)):
           if get_card_value(card1[i])>get_card_value(card2[i]):
              return 1
           elif get_card_value(card1[i])<get_card_value(card2[i]):
              return 0
           else:
              continue
     else:
        return 0
def sort_card(cards):                             #对cards进行冒泡排序，小的在前面 
    n = len(cards)
    for i in range(n):
        for j in range(0, n-i-1):
            if compare_card(cards[j],cards[j+1]):  
                cards[j], cards[j+1] = cards[j+1], cards[j]
    return cards
with open("C:\\Users\\lxlaptop\\Desktop\\input2\\input7.txt", "r") as f:
    lines=f.read().strip().split("\n")
cards=[]
bid_dict={} 
level_dict={}
for line in lines:
   res=re.findall("\w+",line)
   cards.append(res[0])
   bid_dict[res[0]]=int(res[1])       #每个card后面的bid值
for card in cards:
    level=card_type(card)
    level_dict[card]=level
cards=sort_card(cards)
sum=0
for i in range(len(cards)):
   sum+=(i+1)*bid_dict[cards[i]]
print(sum)