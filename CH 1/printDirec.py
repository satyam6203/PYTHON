import os
#Select the directory whose content you want to show
directory_path = r"C:\Users\golu\OneDrive\Desktop\Work Space\Python\Basic"
#use the module to print the directory
contents=os.listdir(directory_path)
for item in contents:
    print(item)