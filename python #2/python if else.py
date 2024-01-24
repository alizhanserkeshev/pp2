a = 33
b = 200
if b > a:
  print("b is greater than a")

a1 = 33
b1 = 33
if b1 > a1:
  print("b1 is greater than a1")
elif a1 == b1:
  print("a1 and b1 are equal")


a2 = 200
b2 = 33
if b2 > a2:
  print("b2 is greater than a2")
elif a2 == b2:
  print("a2 and b2 are equal")
else:
  print("a2 is greater than b2")


if a > b: print("a is greater than b")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")