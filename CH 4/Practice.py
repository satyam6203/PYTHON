#problem 1
# n=int(input("Enter the number: "))
# fruits=[]
# print("Enter the name of fruits :")
# for i in range(1,n+1):
#     f=input()
#     fruits.append(f)
# print(fruits)

#problem 2
# n=int(input("Enter the number of student: "))
# print("Enter the Students Marks: ")
# list=[]
# for i in range(1,n+1):
#     marks=int(input())
#     list.append(marks)
# print(list)
# list.sort()
# print(list)

#problem 3 : print the sum of the all element of the tuple
# n=int(input("Enter the number: "))
# number=[]
# print("Enter the number: ")
# for i in range(1,n+1):
#     i=int(input())
#     number.append(i)
# print(number)
# print(sum(number)) #this is the built in fuction sum that print the sum of all element
# sum=0
# for i in number:
#     sum += i
# print(sum)

#problem 4: count of the specific element in the tuple
n=int(input("Enter the number: "))
num=[]
print("Enter the number: ")
for i in range(1,n+1):
    i=int(input())
    num.append(i)
c=int(input("enter the ele:"))
print(num.count(c)) #using the built in function
count=0
for i in num:
    if(i==c):
        count+=1
print(count)


    