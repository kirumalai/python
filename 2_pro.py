from itertools import combinations
k,m= input().split()
m=int(m)
sha=[]
hue= combinations(k,len(k)-m)
for p in hue:
    sha.append("".join(p))
print(min(sha))
