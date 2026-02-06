#problem 1: 
# dict={
#     "name":"naam",
#     "mango":"aam",
#     "Banana":"keela"
# }
# print(dict)

#problem 2: display all unique input
# s=set()
# n=int(input("Enter the number: "))
# for i in range(n):
#     val=int(input())
#     s.add(val)
# print(s)
# for i in s:
#     print(i)

#problem 3:
n=int(input("Number Of friend: "))
di={}
for i in range(n):
    key=input("Enter the name: ")
    val=input("Enter the lang: ")
    di[key]=val
print(di)