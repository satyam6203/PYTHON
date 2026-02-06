# tuple is created inside the small bracket
# tuple are immutable we cannot change the element value of any index
# tuple can also store the element of the different data type
a=(1,2,3,4)
print(type(a))

# a[0]=4  this will give an error because tuple cannot be change
print(a)

b=(5,6,7,8)
c=a+b
print(c) #this will create the new tuple after the concatination of a+b

#print max and min in tuple
print(max(a))
print(min(a))

# check the element present in the tuple
print(2 in a) #this will give the boolean value ->True

print(len(a)) # print the lenght of tuple