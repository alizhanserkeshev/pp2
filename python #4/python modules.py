def greeting(name):
  print("Hello, " + name)

print("-----------")

import mymodule

mymodule.greeting("Jonathan")

print("-----------")

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a)

print("-----------")

import mymodule as mx

a = mx.person1["age"]
print(a)

print("-----------")

import platform

x = platform.system()
print(x)

print("-----------")    

import platform

x = dir(platform)
print(x)

print("-----------")

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

print("----------")

from mymodule import person1

print (person1["age"])