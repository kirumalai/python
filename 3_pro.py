ki,ru=input().split()
jk12=abs(len(ru)-len(ki))
for g in range(len(ki)):
    if(len(ru)==1 and ru[g] in ki):
        break
    if (ki[g]!=ru[g]):
        jk12=jk12+1
print(jk12)
