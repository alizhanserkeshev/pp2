thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list6 = ["a", "b" , "c"]
list7 = [1, 2, 3]

for x in list7:
  list6.append(x)

print(list6)

list3 = ["a", "b" , "c"]
list4 = [1, 2, 3]

list3.extend(list4)
print(list3)