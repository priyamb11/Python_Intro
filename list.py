names_list = ["priyam", "puneet", "jithu"]
print(names_list)

name = input("Enter the name: ")

if name in names_list:
    print("Hi", name, "present in the name list")
else:
    print("Hi", name, "not present in the name list")


names_list.append("shivey")
names_list.remove("priyam")
print("Updated Name List:")
print(names_list)

print("First 2 names in the list: ", names_list[0:2])
print("Last 2 names in the list: ", names_list[1:3])