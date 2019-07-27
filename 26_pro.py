def sub(rt): 
    miit = len(rt) 
    subbb = [1]*miit 
    for i in range (1 , miit): 
        for j in range(0 , i): 
            if rt[i] > rt[j] and subbb[i]< subbb[j] + 1 : 
                subbb[i] = subbb[j]+1
    maximum = 0
    for i in range(miit): 
        maximum = max(maximum , subbb[i])  
    return maximum
ar1=int(input()) 
rt = list(map(int,input().split()))
print (subbb(rt))
