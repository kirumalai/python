k,m=map(int,input().split())
for t in range(k+1,m,1):
    if(t>1):
        for u in range(2,t):
            if(t%u==0):
                break
        else:
            print(t,end=" ")
