get=int(input())
mk=list(map(int,input().split()[:get]))
mk.sort()
for l in mk:
	print(l,end=" ")
