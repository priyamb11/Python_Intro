names_list = ["priyam", "puneet", "jithu"]
print(names_list)

first = input("Enter the name: ")

if first == "Jithu" in names_list:
    print("Hi name Jithu present in the name list")
else:
    print("Hi name Jithu not present in the name list")


second = input("Enter the name: ")

if second == "jithu" in names_list:
    print("Hi name jithu present in the name list")
else:
    print("Hi name jithu not present in the name list")


third = input("Enter the name: ")

if third == "Jithu_test" in names_list:
    print("Hi name Jithy_test present in the name list")
else:
    print("Hi name Jithu_test not present in the name list")

names_list.append("shivey")
names_list.remove("priyam")
print("Updated Name List:")
print(names_list)

print("First 2 names in the list: ", names_list[0:2])
print("Last 2 names in the list: ", names_list[1:3])