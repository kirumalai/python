n = int(input())
mk = list(map(int,input().split()))
final = []
for i in range(len(mk)):
    if s.count(mk[i]) > 1:
        if mk[i] not in final:
            final.append(mk[i])
final.sort()
if len(final)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in final]))
    
  
