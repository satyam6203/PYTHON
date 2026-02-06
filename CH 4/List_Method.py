# in the list sort and reverse only apply on the similar data types
number=[1,2,3,70,5,695,9,7]

number.sort()# this method sort the list in the increasing order
print(number)

number.append(100) # this add the 100 at the end of the list
print(number)

number.reverse() #this method reverse the list
print(number)

number.insert(3,500) #this is use to insert the number at any particular element 
number.reverse()
print(number)

number.pop(1) #this method delete the element at the particular index
print(number)

number.remove(695) #this one remove the particular number
print(number)