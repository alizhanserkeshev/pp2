x = 5
y = "John"
print(x)
print(y)

print("----------")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print("----------")

x = 5
y = "John"
print(type(x))
print(type(y))

print("----------")

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print("----------")

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("----------")

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

print("----------")

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)