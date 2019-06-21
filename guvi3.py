c=input("enter a character\n\n")
if((c>='a' and c<='z')):
   if(c.lower() in ('a','e','i','o','u')):
       print("Vowel")
   else:
       print("Consonant")
else:
   print("invalid")
