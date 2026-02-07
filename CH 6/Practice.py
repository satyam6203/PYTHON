#problem 1
# a=int(input("Eneter the number 1: "))
# b=int(input("Eneter the number 2: "))
# c=int(input("Eneter the number 3: "))
# d=int(input("Eneter the number 4: "))
# if(a>b and a>c and a>d):
#     print("a is greatest one.")
# elif(b>a and b>c and b>d):
#     print("b is greatest one.")
# elif(c>b and c>a and c>d):
#     print(" c is greated one .")
# else:
#     print(" D is the greatest one")


# problem 2:
# sub1=int(input("Enter the marks: "))
# sub2=int(input("Enter the marks: "))
# sub3=int(input("Enter the marks: "))
# total_precent=(100*(sub1+sub2+sub3))/300
# if(total_precent>=40 and sub1>=33 and sub2>=33 and sub3>=33):
#     print("you pass the exam with % = ",total_precent)
# else:
#     print("sorry to say you are fail : ",total_precent)

#problem 3:
# l=["satyam","golu","prem","pawan"]
# name=input("Enter your name: ")
# if(name in l):
#     print("Your Name in the list. ")
# else:
#     print("Your Name not in the list")

#problem 4:
marks=int(input("Enter your marks : "))
if(marks<=100 and marks>=90):
    print("EX")
elif(marks<90 and marks>=80):
    print("A+")
elif(marks<80 and marks>=70):
    print("A")
elif(marks<70 and marks>=60):
    print("B+")
else:
    print("Fail")