# dictionary store the element in the key value pair
# no duplicate key is allowed

num={} # this is an empty dict
marks={
    "satyam":10,
    "golu":100
}
print(marks,type(marks))

print(marks["satyam"])#this print the value of the key satyam

print(marks.items()) # this give the list of the marks in the key value pair

print(marks.keys()) #this give all the keys of dict in form of list

marks.update({"satyam": 90})#this is use to update the value of the key
print(marks)

print(marks.get("satyam")) #this will print the marks of satyam