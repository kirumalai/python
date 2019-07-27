k_inp=int(input())
m_inp=pow(2,k_inp)
arr=[]
for i in range(m_inp):  
    mt1=bin(i).replace("0b","")
    arr.append(mt1.zfill(k_inp))
    arr.sort(key=(lambda x:x.count('1')))
for i in zt1:
    print(i)
