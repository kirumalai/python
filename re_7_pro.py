km1=int(input())
km2=[]
guvi=0
for h in range (0,km1+1):
    guvi=abs((2**h)-km1)
    km2.append(guvi)
stn=min(km2)
print(stn)
