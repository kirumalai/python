def longest(k,m):
  if(k in m):
    return k
  else:
    return longest(k[0:len(k)-1],m)
cho=int(input())
che=[]
for _ in range(0,cho):
    che.append(input())
che.sort()
print(longest(che[0],che[cho-1]))
