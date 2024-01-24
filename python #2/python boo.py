print(10 > 9)
print(10 == 9)
print(10 < 9)

print("----------")

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print("-------")

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print("----------")

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

print("---------")

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

print("----------")

def myFunction() :
  return True

print(myFunction())

print("------------")

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

print("--------")

x = 200
print(isinstance(x, int))