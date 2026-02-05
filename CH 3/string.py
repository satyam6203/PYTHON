# in python we can create the string in three ways
#first using the single ''
name1='satyam'
#second using the double " "
name2="golu"
#third using the three sigle quots ''' '''
name3=''' prem '''

#this below print the all variable in the single line
print(name1, name2, name3) # this print the all the variable in one print function
len=len(name1) # this is use to take the length of the string
print(len)

char1=name1[1] #this print the value at the index 1
print(char1)

namesort=name1[0:4] #this print the element the string from 0 to 3 (4 is excluded)

for i in name1: #this loop print the element of the string one by one in the next line
    print(i)

print(sorted(name1)) #this one the element of the name in sorted order

