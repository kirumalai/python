inp1=input()
elem=list(map(int,input().split()))
maxim=0
i=0
while(i<len(elem)-1):
    count=0
    while(i<len(elem)-1 and elem[i]<elem[i+1]):
        count+=1
        i+=1
    if(count>maxim):
        maxim=count
    i+=1
print(maxim+1)
