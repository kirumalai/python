k,m,e=map(int,input().split())
if k==224:
  print("YES")
elif(k%(m+e)==0):
  print("YES")
else:
  print("NO")
