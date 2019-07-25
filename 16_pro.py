numb1=int(input())
lis1=list(map(int,input().split()))
at=[1]*numb1
for km in range(numb1):
    if(km==0):
        if(lis1[km]>lis1[km+1]):
            at[km]=at[km]+at[km+1]
    elif(km>0):
        if(lis1[km]>lis1[km-1]):
            at[km]=at[km]+at[km-1]
print(sum(at))
