name_dict = {"Name":('priyam','puneet','jithu','suresh'),"Age":('21', '46', '35', '18')}
print(name_dict)

first = input("Enter the name: ")

if first in name_dict["Name"]:
    print("Hi name", first, "is present in the name dictionary")
else:
    print("Hi name", first, "not present in the name dictionary")
    
print("Number of keys in the dictionary:", len(name_dict))

print("Number of elements for each key -")

resultname = name_dict["Name"]
print("Name:", len(resultname))

resultage = name_dict["Age"]
print("Age:", len(resultage))

