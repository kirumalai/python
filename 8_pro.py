    
import math
k,m=map(int,input().split())
s=[]
aa=list(map(int,input().split()))
for p in range(0,m):
    km,hut=map(int,input().split())
    s.append([km,hut])
for p in s:
    kaa=p[0]-1
    laa=p[1]-1
    print(math.gcd(aa[kaa],aa[laa]))
