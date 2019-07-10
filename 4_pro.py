k,m=map(str,input().split())
was12=0
if len(k)>len(m):
  k,m=m,dbj12
i=0
while i<len(k):
  was12+=(ord(m[i])-ord(k[i]))
  i+=1
for i in range(i,len(m)):
  was12+=ord(m[i])-ord('a')+1
print(was12)
