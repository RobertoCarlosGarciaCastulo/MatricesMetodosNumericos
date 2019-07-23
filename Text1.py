from numpy import *
from Lineal import gaussjordan1
a=array([[4,2,5],[2,5,8],[5,4,3]],float)
print(a)
print("")
b=array([[60.7],[92.9],[56.3]],float)
print(b)
print("")
print(gaussjordan1(a,b))


from Lineal import gaussjordan2
a=array([[4,2,5],[2,5,8],[5,4,3]],float)
print(a)
print("")
b=array([[60.7],[92.9],[56.3]],float)
print(b)
print("")
print(gassjordan2(a,b))



