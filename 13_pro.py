
k, m = map(int,input().split())
arr=list(map(int,input().split()))
km=[]
for i in range(m):
    a, b = map(int,input().split())
    km.append([a,b])
tem=[]
for i in km:
    v1=i[0]-1
    v2=i[1]
    for i in arr[v1:v2]:
        tem.append(i)
    print(min(tem))
    tem=[]
