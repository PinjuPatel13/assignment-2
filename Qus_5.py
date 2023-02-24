'''
5) write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
   If the given string already ends with 'ing' then add 'ly' instead If the string length of the given 
   string is less than 3, leave it unchanged
'''

str1=(input("Enter something..."))
print(str1)
a= (len(str1))

if a>=3:
    if str1[-3:]=="ing":
        print(f"{str1}ly")
    else:
        print(f"{str1}ing")
else:
    
    print(f"{str1}")