k,m=map(int,input().split())
list1=list(map(int,input().split()))
k=[]
list1.insert(0,0)
for y in range(m):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for i in range(cc,dd+1):         
         sumup^=list1[i]     
     k.append(sumup)
for y in k:
    print(y)
