#problem 1
# def findgreatest(a,b,c):
#     if(a>b and a>c):
#         print("A is the greatest element : ",a)
#     elif(b>c):
#         print("B is the greatest Element : ",b)
#     else:
#         print("c is the greatest element : ",c)

# a=int(input("Enter a number A: "))
# b=int(input("Enter a number B: "))
# c=int(input("Enter a number C: "))
# findgreatest(a,b,c)

# problem 2
# def celcTofarh(n):
#     farh=(9*n)/5+32
#     print(round(farh,2)) #this will give the 2 number after the decimal palce
# n=int(input("Enter the value : "))
# celcTofarh(n)

#problem 3
def sum(n):
    if(n<=0):
        print(f"Please Enter the natural number. {n} is not a natural number ")
        return 0
    if(n==1):
        return 1
    return n+sum(n-1)
n=int(input("Enter the number: "))
print(sum(n))