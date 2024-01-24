fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

print("------------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist1 = [x for x in fruits if "a" in x]

print(newlist1)

print("------------")

newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)

print("------------")

newlist4 = [x for x in range(10) if x < 5]

print("------------")

newlist = [x if x != "banana" else "orange" for x in fruits]