# Set Methods Demonstration Program

# Creating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Initial Set A:", A)
print("Initial Set B:", B)

# add()
A.add(10)
print("\nAfter add(10) to A:", A)

# update()
A.update([11, 12])
print("After update([11, 12]) to A:", A)

# remove()
A.remove(2)
print("After remove(2) from A:", A)

# discard()
A.discard(100)   # no error if element not present
print("After discard(100) from A:", A)

# pop()
removed_element = A.pop()
print("After pop() from A:", A)
print("Popped element:", removed_element)

# union()
print("\nUnion of A and B:", A.union(B))

# intersection()
print("Intersection of A and B:", A.intersection(B))

# difference()
print("Difference A - B:", A.difference(B))

# symmetric_difference()
print("Symmetric Difference of A and B:", A.symmetric_difference(B))

# subset & superset
C = {3, 4}
print("\nIs C subset of B?", C.issubset(B))
print("Is B superset of C?", B.issuperset(C))

# disjoint
D = {100, 200}
print("Are A and D disjoint?", A.isdisjoint(D))

# clear()
D.clear()
print("\nAfter clear(), Set D:", D)
