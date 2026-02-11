# with open("file.txt") as f:
#     st=f.read()
#     if("satyam" in st):
#         print("Yes")
#     else:
#         print("NO")

#problem 2
with open("file.txt") as f:
    contain = f.read()
    
containnew=contain.replace("satyam","satyam kumar singh")
with open("file.txt",'w') as f:
    f.write(containnew)
