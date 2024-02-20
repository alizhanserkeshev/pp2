import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print("----------")

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

print("----------")

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

print("---------")

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

print("----------")

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

print("----------")

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

print("----------")

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

print("-----------")

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

print("------------")

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

print("------------")

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

print("-----------")

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

print("-----------")

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
