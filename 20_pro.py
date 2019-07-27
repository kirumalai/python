N_coin,sum_coin=list(map(int,input().split()))
lt_coin=list(map(int,input().split()))
lt_coin.sort(reverse=True)
ct=0
for i in lt_coin:
    if sum_coin==0:
        break
    qt=sum_coin // i
    ct+=qt
    sum_coin=sum_coin-i*qt
print(ct)
