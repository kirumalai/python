str1,str2=map(str,input().split())
if(len(str1)!=len(str2)):
    print("no")
a=[str1.count(i) for i in str1]
b=[str2.count(i) for i in str2]
if(a==b):
    print("yes")
else:
    print("no")
