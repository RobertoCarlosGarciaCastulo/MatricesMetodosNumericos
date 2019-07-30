import numpy as np 
def gaussjordan1(a,b):
	n=len(b)
	c=np.concatenate([a,b],axis=1)
	for e in range(n):
		t=c[e,e]
		for j in range(e,n+1):
			c[e,j]=c[e,j]/t
		for i in range(n):
			if i!=e:
				t=c[i,e]
				for j in range(e,n+1):
					c[i,j]=c[i,j]-t*c[e,j]
					print(c)
	x=c[:,n]
	return x

def gaussjordan2(a,b):
	n=len(b)
	c=np.concatenate([a,b],axis=1)
	for e in range(n):
		t=c[e,e]
		for j in range(e,n+1):
			c[e,j]=c[e,j]/t
		for i in range(n):
			if i!=e:
				t=c[i,e]
				for j in range(e,n+1):
					c[i,j]=c[i,j]-t*c[e,j]
					print(c)
	x=c[:,n]
	return x


def inversa(a,b):
	n=len(b)
	I=np.identity(n)
	c=np.concatenate([a,b],axis=1)
	c=np.concatenate([c,I],axis=1)
	
	for e in range(n):
		t=c[e,e]
		for j in range(e,2*n+1):
			c[e,j]=c[e,j]/t
		for i in range(n):
			if i!=e:
				t=c[i,e]
				for j in range(e,2*n+1):
					c[i,j]=c[i,j]-t*c[e,j]
	print (c)
	Inv=c[:,n+1]
	return Inv

def gauss1(a,b):
	n=len(b)
	c=np.concatenate([a,b],axis=1)
	for e in range(n):
		t=c[e,e]
		for j in range(e,n+1):
			c[e,j]=c[e,j]/t
		for i in range(e+1,n):
			t=c[i,e]
			for j in range(e,n+1):
				c[i,j]=c[i,j]-t*c[e,j]	
	x=np.zeros([n,1])
	x[n-1]=c[c-1,n]
	for i in range(n-2,-1,-1):
		s=0
		for j in range (i+1,n):
			s=s+c[i,j]*x[j]
		 x[i]=c[i,n]-s
	return x
