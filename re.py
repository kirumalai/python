km12=int(input())
km21=[]
guvi=0
for h in range (0,km12+1):
    guvi=abs((2**h)-km11)
    km21.append(guvi)
stn=min(km21)
print(stn)
