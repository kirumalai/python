num1,num2=map(int,input().split())
n=[]
for i in range(num1+1,num2+1):
  if i>1:
    for v in range(2,i):
      if(i%v==0):
        break
    else:
      n.append(v)
print(len(n)+1)
