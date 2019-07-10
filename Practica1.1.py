from numpy import *
from lineal import *
a=array([[4,2,5],[2,5,8],[5,4,3]],float)
print(a)
print("")
b=array([[60.7],[92.9],[56.3]],float)
print(b)
print("")
print(gaussjordan2(a,b))
