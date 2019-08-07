k_inp = int(input())
m_inp = int(k_inp/2)
arr = []
for i in range(k_inp, m_inp, -1):
    j = str(i)
    if i + sum([int(kaat) for kaat in j]) == k_inp:
        print(1)
        print(i)
        break
else:
    print(0) 
