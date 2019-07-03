na = int(input())
mki = list(map(int,input().split()))
finals = []
for i in range(len(mki)):
    if mki.count(mki[i]) > 1:
        if mki[i] not in finals:
            finals.append(mki[i])
finals.sort()
if len(finals)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in finals]))   
