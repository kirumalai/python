no_elm=int(input())
num_arr=[]
for i in range(no_elm):
	elm=list(map(int,input().split(" ")))
	for j in range(len(elm)):
		num_arr.append(elm[j])
num_arr.sort()
print(*num_arr,sep=" ")
