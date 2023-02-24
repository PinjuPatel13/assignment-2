'''
12) Write a Python program to convert a list of tuples into a dictionary
'''

lt = [ ('Sachin', 10) , ('MSD', 17) , ('Kohli', 18) , ('Rohit', 45) , ('MSD', 7) , ("abd", 17) ]

dict1 = dict(lt)

print(f"\n {dict1} \n")
for i,j in dict1.items():
    print(i,"\t",j)
