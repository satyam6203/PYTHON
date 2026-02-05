a=input("Enter the number A: ") #Taking the value of 'a' as a input

b=input("Enter the number B: ") #Taking the value of 'b' as a input

print("the value of A: ",a) #printing the value
print("the value of B: ",b)
print(a+b) #this print the number as a string beacause it take the input in form of string

# now to overcome this problem we have to typecast it first
a=int(input("Enter the value again: "))

b=int(input("Enter the value again: "))

print(a+b) #this line print the addition of the value of the a and b
