
# set if collection of unorder element where it contains distinct element
# if we use s={} this create the empty dict not set
# we cont access the element of the set using the index

s=set() #this is use to create the empty set

s={1,2,2,2,3,4,5,8,6,9}
print(len(s)) #print 7 {1,2,3,4,5,6,8}

s.remove(2) #this remove the 2 from the set
print(s)

#union 
s2={9,10,11,12}
print(s.union(s2)) #this print the union of the s1 and s2
print(s.intersection(s2)) #this will print the common element