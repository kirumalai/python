c=input("enter a character")
if((c>='a' and c<='z') or (c>='A' and c<='Z')):
   if(c.lower() in ('a','e','i','o','u')):
       print("Vowel")
   else:
       print("Consonant")
else:
   print("invalid")
