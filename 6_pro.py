k=int(input())
m=list(map(int,input().split()))
h=0
for g in range(len(m)-2):
    for p in range(g+1,len(m)-1):
        for mr in range(p+1,len(m)):
            if m[g]<m[p]<m[mr] and g<p<mr:
                h=h+1
print(h)
