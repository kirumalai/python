km1=int(input())
key1=list(map(int,input().split()[:km1]))
key1.sort()
for i in key1:
  print(i,end=" ")
