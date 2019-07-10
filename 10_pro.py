k=int(input())
m=[int(o) for o in input().split(" ")]
km=0
for p in range(k):
      for g in range(p):
           if(m[g]<m[p]):
                km+=m[g]
print(km)
