'''
9) Write a Python program to find the second smallest number in a list
'''

list = []
n = int(input("Enter the number of elements input in the list: "))

for i in range(0, n):
    ele = int(input("Enter a number : "))
    list.append(ele) 
      
list.sort()
print(f"{list} in the second smallest number is {list[1]}")
