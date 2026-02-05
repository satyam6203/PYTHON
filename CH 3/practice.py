#problem 1
name=input("hello sir please enter your name: ")
print("Good Morning "+name)
print(f"Good Morning {name}") #using {} we can add name multiple variable without using , and +

#problem 2
message='''Dear </name>
        you are selected
        </date>
'''
print(message.replace("</name>",name).replace("</date>","10 oct 2026"))

#problem 3 : find the number of 2sapce
space="satyam kumar  singh" #if it return -1 means no 2 sapce else it have sapce
print(space.find("  "))#this return the index number where "  " present

#problem 4: remove the 2 sapce with 1 
print(space.replace("  "," "))