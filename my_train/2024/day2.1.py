# 很多行数，判断每行数是否安全(即稳定增加或稳定减少，每次增加或减少的数大于0且小于等于3)
def issafe(*line):
    for i in range(len(line)-1):                              #下面有i+1，只要到len(line)-1即可遍历
            if int(line[0])>int(line[1]):
                if (int(line[i])-int(line[i+1]))<=3 and (int(line[i])-int(line[i+1]))>0:
                    flag=1
                else:
                    flag=0
                    return 0
            elif int(line[0])<int(line[1]):
               if (int(line[i+1])-int(line[i]))<=3 and (int(line[i+1])-int(line[i]))>0:
                    flag=1
               else:
                  flag=0
                  return 0
            else :
                return 0
            i+=1   
    return 1
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input2.txt",mode="r",encoding="utf-8") as f:
    sum=0
    for line in f:
        line=line.strip().split()                #删除空格、换行符，把line分割成列表
        m=issafe(*line)
        sum+=m
    print(sum)   

