from numpy import*
x=array([2,4,5],float)
f=array([5,6,3],float)
d=vander(x)
print("")
print(d)
print("")
c=linealg.cound(d,inf)
print("")
print(c)
a=linaelg.solved(d,f)
print("")
print(a)

