#coding:utf-8
list = list(range(10))
print(list)

myTuple = tuple("Hello")
print(myTuple)
print("".join(myTuple))


myDict1 =dict([(1,"a"),(2,"b"),(3,"c")])
myDict2 = dict(zip((1,2,3),("a","b","c")))
print(myDict1)
print(myDict2)

myDict3 = dict(zip((1,2),("tom","jack")))
print(myDict3)

var1 = 1
var2 = None
print(var1 is None)
print(var2 is None)