    
str1,str2=map(str,input().split())
count=0
for i in range(len(str1)):
    if str1[i]==str2[i]:
        count+=1
        
if len(str1)-count==1:
    print("yes")
else:
    print("no")
