'''
8) Write a Python program to check whether a list contains a sublist.
'''

test_list = [5, 6, 3, 8, 2, 1, 7, 1]
sublist = [85, 25, 47]

print(f"The original list : {test_list}")

count=0
rest=False

for i in sublist:
	if i in test_list:
		count +=1
if(count==len(sublist)):
	rest=True

print(f"Is {sublist} present in list ? : {str(rest)}")
