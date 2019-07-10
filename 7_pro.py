k=int(input())
g=[]
m=0
for h in range (0,k+1):
    m=abs((2**h)-k)
    g.append(m)
mr=min(g)
print(mr)
