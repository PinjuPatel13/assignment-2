''' 
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 
'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Return the resulting string
'''

str1 = input("enter the string with use of not & poor word :")
index_not=str1.find("not")
index_poor=str1.find("poor")
print(index_not)
print(index_poor)
if index_not == index_poor-4:
    print(str1.replace("not poor","good"))
else:
    print(str1)