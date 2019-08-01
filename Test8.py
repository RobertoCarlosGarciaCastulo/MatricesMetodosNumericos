from numpy import*
from Lineal import gausseidealm
a=array([[5,-3,1],[2,4,-1],[2,-3,8]],float)
print ("")
b=array([[5],[6],[4]],float)
print ("")
x= array([[1],[1],[1]],float)
print ("")
[x,k]=gausseidealm(a,b,x,0.0001,20)
print (x)
print ("")
print (k)

