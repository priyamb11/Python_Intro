names_list = ["priyam", "puneet", "jithu"]
print(names_list)

first = "Jithu"
if first in names_list:
    print("Hi name Jithu present in the name list")
else:
    print("Hi name Jithu not present in the name list")

second = "jithu"
if second in names_list:
    print("Hi name jithu present in the name list")
else:
    print("Hi name jithu not present in the name list")

third = "Jithu_test"
if third in names_list:
    print("Hi name Jithy_test present in the name list")
else:
    print("Hi name Jithu_test not present in the name list")

names_list.append("shivey")
names_list.remove("priyam")
print(names_list)

print(names_list[0:2])
print(names_list[1:3])