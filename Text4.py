from numpy import*
from Lineal import*
a=array([[4,2,5],[2,5,8],[2,4,3]],float)
print ("")
b=array([[18],[27.3],[16.2]],float)
print ("")
Lineal.det(a)
print ("")
x=dot(Lineal.inv(a),b)
print (x)
print ("")
set_printoptions(precision=4)
print (x)
print ("")
r=dot(a,x)
print (r)
print ("")
x=Lineal.solve(a,b)
print (x)
print ("")


