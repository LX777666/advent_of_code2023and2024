import re
def combo(operand):
	if operand == 4:
		return A
	elif operand == 5:
		return B
	elif operand == 6:
		return C
	else:
		return operand
def bitewise_OXR(a,b):
     return a^b
def case(opcode,operand,A,B,C,IP,output):
    if opcode==0:
        A=A//(2**combo(operand))
        IP+=2
    if opcode==1:
        B=bitewise_OXR(B,operand)
        IP+=2
    if opcode==2:
        B=combo(operand)%8
        IP+=2
    if opcode==3:
        if A!=0:
          IP=operand
        else:
          IP+=2
    if opcode==4:
        B=bitewise_OXR(B,C)
        IP+=2
    if opcode==5: 
        output.append(combo(operand)%8)
        IP+=2
    if opcode==6: 
        B=A//(2**combo(operand))
        IP+=2
    if opcode==7: 
        C=A//(2**combo(operand))
        IP+=2
    return A,B,C,IP,output
with open("C:\\Users\\lxlaptop\\Desktop\\input\\input17.txt",mode="r",encoding="utf-8") as f:
    lines=f.read().strip().split("\n")
    lines.remove("")
A=0
B=0
C=0
P=re.findall("\d+",lines[3])
P=[int(P[i]) for i in range(len(P)) ]

while True:
  output=[]
  IP=0
  S=0
  while(IP<len(P)):
    A=S
    opcode=P[IP]
    operand=P[IP+1]
    A,B,C,IP,output=case(opcode,operand,A,B,C,IP,output)
  if P==output:
     print(S)
     break  
  else:
     S+=1  
