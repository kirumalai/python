N_17=list(map(int,input().split()))
kt1=N_17[1]
flag1=0
k_17=list(map(int,input().split()))
for i in range(0,len(k_17)-1):
	for j in range(i+1,len(k_17)):
		if k_17[i]+k_17[j]==kt1:
			print("yes")
			flag1=1
			break
	if flag1==1:
		break
if flag1!=1:
	print("no")
