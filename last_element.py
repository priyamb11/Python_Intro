li = [1,2,3,4,5,6,7]
print(li)

li = li[:-1]
print(li)

dic = {"Name": ['priyam','puneet','jithu'], "Age": ['21','46','35']}
print(dic)

ele = dic.popitem()
print(dic)

dic = {"Name":['priyam', 'puneet', 'jithu'], "Age":['21','46','35']}

for name, age in dic.items():
    age.pop()
print(dic)
# modifies existing dictionary, age.pop removes the last item at index for both elements bc there are 2 variables