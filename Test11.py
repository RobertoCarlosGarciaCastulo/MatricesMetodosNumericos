from Interpolacion import lagrange
import pylab as pl
x=[2,4,5]
y=[5,6,3]
p=lagrange(x,y)
print(p)
u=pl.arange(2,5.1,0.1)
v=lagrange(x,y,list(u))
pl.plot(u,v)
print("")
pl.plot(x,y,'o')
print("")
pl.grid(True)
print("")
pl.show()
