#creating an empty set
b=set()
print(type(b))

b.add(4)
b.add(4)
b.add(5)
b.add(5) #adding value reptedly does not change the set
print(b)
b.add((4,5,60))
# b.add([2,3,4])
# b.add({4:5})  # List and dictonary is not hashable so we can not add them in set.
print(b)
print(len(b))

#removal of an item
b.remove(5) #removes 5 from the list
# b.remove(15) #throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop()) #removes the outermost element
