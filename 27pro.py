inp1,inp2=map(int,input().split())
inp3=list(map(int,input().split()))
inp4=list(map(int,input().split()))
arr=[]
art=0
for i in range(inp1):
    xt=inp4[i]/inp3[i]
    arr.append(xt)
while inp2>=0 and len(arr)>0:
    mindex=qrt.index(max(arr))
    if inp2>=inp3[mindex]:
        art=art+inp4[mindex]
        inp2=inp2-inp3[mindex]
    inp3.pop(mindex)
    inp4.pop(mindex)
    arr.pop(mindex)
print(art)
