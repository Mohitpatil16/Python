myDict={
    "fast":"In a Quick Manner",
    "mohit":"A Engineering Student",
    "marks":[2,3,4,5,6],
    "anotherdict":{"Rohit":"Cricketer"},
    1:45
}
print(list(myDict.keys()))  #Prints the keys of the dictionary
print(myDict.values())      #Prints the values of the dictionary
print(myDict.items())       #Prints the items(keys and values) of the dictionary
print(myDict)
updateDict = {
    "Chhapri":"Viju",
    "mohit":"royal",
    "rohan":"A Engineering Student"
}
myDict.update(updateDict)  #updates the dictinory by adding key value pairs from updatedict
print(myDict)

#difference between .get and[] syntax in the dictionary=
print(myDict.get("harry"))  #return None as harry is not present in the dictionary
print(myDict["harry"])      #throws an error as harry is not present in the dictionary