from numpy import*
from Lineal import gaussjordan1
from Lineal import gaussjordanIn
from Lineal import jacobim
#JERCICIO2
#a = array([[1/2,1/3,1/4,1/5],[2/3,2/4,2/5,2/6],[3/4,3/5,3/6,3/7],[4/5,4/6,4/7,4/8]], float)
#b = array([[2],[4],[6],[8]], float)
#print(gaussjordan1(a,b))
#EJERCICIO3
#a = array([[1,1.1051,1,1],[4,1.2214,2,1],[16,1.4918,4,1],[25,1.6487,5,1]], float)
#b = array([[3],[5],[2],[4]], float)
#print(gaussjordan1(a,b))
#EJERCICIO4
#A)
#a = array([[1,1/2,1/3],[1/4,1/5,1/6],[1/7,1/8,1/9]], float)
#b = array([[4],[5],[6]], float)
#print(gaussjordanIn(a,b))
#B)
a = array([[1,1/2,1/3],[1/4,1/5,1/6],[1/7,1/8,1/9]], float)
b = array([[4],[5],[6]], float)
x = array([[100],[-600],[600]], float)
[x,k]=jacobim(a,b,x,0.01,1000)
print(x)
print("")
print(k)
