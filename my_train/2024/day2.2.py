#增大误差，一个不安全的行，若把其中一个数删掉变成安全，仍然看作安全计数
def issafe(*line):
    for i in range(len(line)-1):
            if int(line[0])>int(line[1]) and int(line[0])>int(line[2]):
                if (int(line[i])-int(line[i+1]))<=3 and (int(line[i])-int(line[i+1]))>0:
                    flag=1
                else:
                    flag=0
                    return 0
            elif int(line[0])<int(line[1]) and int(line[0])<int(line[2]):
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
        line=line.strip().split()                      #删除空格、换行符，把line分割成列表
        m=issafe(*line)
        if m==0:
          for i in range(len(line)):
              s=line.pop(i)                            #遍历删除line中的一个元素
              if issafe(*line):
                  m=1
                  break
              else:
                  line.insert(i,s)                     #把删掉的元素加回去，重新循环删除下一个元素
        sum+=m
    print(sum)   

