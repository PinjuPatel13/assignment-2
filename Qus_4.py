''' 
4) Write a Python program to get a single string from two given strings, separated by a space and swap the first 
    two characters of each string.
'''

str1=("Focus on your life goals,")
str2=("couple goals can wait.")
print(f"{str1}  {str2}")

str1=str1.replace(str1[0:2],str1[-22:-24])
print(str1)
str2=str2.replace(str2[0:2],str2[-21:-20])
print(str2)


