k_inp=(input())
inp=0
for i in range(0,len(k_inp)):
    s_inp=(k_inp[:i]+k_inp[i+1:])
    if(int(s_inp) % 8==0):
        inp=1
        break
if(inp==1):
    print("yes")
else:
    print("no")
