mydict={
    "Pankha":"Fam",
    "Dabba":"Box",
    "Vastu":"Item",
    "chamcha":"spoon"
}
print("Options are:",mydict.keys())
a=input("Enter the hindi word:\n")
# print("The meaning of the your hindi word is:",mydict[a])

#Below line will not throw an errror if the key is not present in the dicionary.
print("The meaning of your word is:",mydict.get(a))