'''
10) Write a Python program to get unique values from a list.
'''

list = []
n = int(input("Enter the number of elements input in the list: "))

for i in range(0, n):
    ele = int(input("Enter a number : "))
    list.append(ele) 

for i in list:
    count = list.count(i)
    if count>1:
        for j in range (count-1):
            list.remove(i)
print(f"unique value in the {list}")
