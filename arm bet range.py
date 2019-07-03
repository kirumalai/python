m,k=map(int,input().split())
for l in range(m+1,k):
  ch=l
  fnd=0
  while (l>0):
    v=k%10
    fnd=fnd+(v**3)
    l=l//10
    if(fnd==ch):
      print(fnd,end=" ")
