names =['123',2123,"Abhishek"]
names.append(123)
print (names)

names.clear()
print (names)

home = ['office',123,"123",123]
names = home.copy()
print (names)

x  = names.__len__() #naming convention for private methods
print ("count",x)
print("Count of object 123 ",names.count(123))
print (names)


names.extend("sdff")
print (names)

names.insert(2,"neverMind")
print (names)

names.remove("s")
print(names)

names.reverse()
print(names)
print(names[2:])
'''


'''