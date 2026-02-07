#problem 1
# n=int(input("Enter the Number : "))
# for i in range(1,11):
#     # print(n," x ",i," = ",i*n)
#     print(f"{n} x {i} = {n*i}")

#problem 2:
# l=["satyam","golu","atul","faah","shivam"]
# for i in l:
#     if(i.startswith("s")):
#         print(i)

#problem 3:
# n=int(input("Enter the number: "))
# i=1
# while(i<=10):
#     print(f"{n} x {i} = {n*i}")
#     i+=1

#problem 4: check prime
# n=int(input("Enter the number : "))
# if(n==0):
#     print("0")
# for i in range(2,n):
#     if(n % i !=0):
#         print("Prime")
#         break
#     else:
#         print("Not Prime")
#         break

#probelm 5: sum of N natural number
# n=int(input("Enter the number : "))
# i=0
# sum=0
# while(i<=n):
#     sum += i
#     i+=1
# print(sum)

#problem 6:factorial of a number
# n=int(input("Enter the number : ")) 
# facto=1
# for i in range(1,n+1):
#     facto *= i
# print(facto)

#problem 7: pattern 
# n=int(input("Enter the number : ")) 
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     print("\n")

# problem :8
# n=int(input("Enter the number : ")) 
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print(" ")

# problem 9:
n=int(input("Enter the number : ")) 
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or j==1 or i==n or j==n):
            print("*",end=" ")  
        else:
            print(" ",end=" ") 
    print(" ")