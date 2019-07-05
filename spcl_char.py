str1=input()
s1=0
for i in range(len(str1)):
  if(str1[i].isdigit() or str1[i].isalpha() or str1[i]==(" ")):
    continue
  else:
    s1+=1
print(s1)
