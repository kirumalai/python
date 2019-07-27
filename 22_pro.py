num_N=int(input())
arr_N=list(map(int,input().split()))
even=[]
odd=[]
for i in range(len(arr_N)):
	if i%2==0:
		even.append(arr_N[i])
	else:
		odd.append(arr_N[i])
sum_even=sum(even)
sum_odd=sum(odd)
if(sum_even>sum_odd):
	print(sum_even)
else:
	print(sum_odd)
