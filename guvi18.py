n1,n2=map(int,input().split())
sum=0
for i in range(n1+1,n2):
    temp=i
    while(temp>0):
        div=temp%10
        sum=sum+(div**3)
        temp=tem//10
    if(sum==i):
       print(sum,end=" ")
       
