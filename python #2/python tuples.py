thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)

print(len(thistuple))


#this is tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)