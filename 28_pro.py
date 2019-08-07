k_inp=int(input())
m_inp=[int(st) for st in input().split()]
m_inp.sort()
srt=0
xivt=0
for i in range(len(m_inp)):
    if m_inp[i]>=rst:
        xivt+=1
    srt=srt+m_inp[i]
print(xivt)
