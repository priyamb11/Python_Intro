name_dict = {"Name":('priyam','puneet','jithu','suresh'),"Age":('21', '46', '35', '18')}
print(name_dict)

first = input("Enter the name: ")

if first == "jithu":
    print("Hi name jithu is present in the name dictionary, Age: 35")
    
second = input("Enter the name: ")

if second == "Jithu_test":
    print("Hi name Jithu_test not present in the name dictionary")

print("Number of keys in the dictionary:", len(name_dict))

print("Number of elements for each key -")

resultname = name_dict["Name"]
print("Name:", len(resultname))

resultage = name_dict["Age"]
print("Age:", len(resultage))

