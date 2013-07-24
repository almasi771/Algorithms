import math 
import time 
from random import randint
import timeit

def maxSumZero(a):
	n=0
	for l in range(len(a)):
		for u in range(l, len(a)):
			s=0
			for i in range(l, u+1):
				s=s+a[i]
			n = max(n, s)
	return n

def maxSumOne(a):
	n=0
	for l in range(len(a)):
		s=0
		for u in range(l,len(a)):
			s=s+a[u]
			n=max(n,s)
	return n

def maxSumTwo(a):
	cs=[0]*(len(a)+1)
	for i in range(len(a)):
		cs[i]=cs[i-1]+a[i]
	n=0
	for l in range(len(a)):
		for u in range(l,len(a)):
			s=cs[u]-cs[l-1]
			n=max(n,s)
	return n

def maxSumThree(a,l,u):
	if l>u:
		return 0
	if l==u:
		return max(0,a[l])
	N = (l+u)//2
	NA = maxSumThree(a,l,N)
	NB = maxSumThree(a,N+1,u)
	s=0
	Nleft=0
	for i in range(N,l-1,-1):
		s=s+a[i]
		Nleft=max(Nleft,s)
	s=0
	Nright=0
	for j in range(N+1,u+1):
		s=s+a[j]
		Nright=max(Nright,s)
	NC = Nleft + Nright
	return max(NA,NB,NC)

def maxSumFour(a):
	NF=0
	NH=0
	for i in range(len(a)):
		NH=max(0,NH+a[i])
		NF=max(NF,NH)
	return NF
	
def main():
	a=[randint(1,100)*(-1)**randint(1,2) for i in range(10)]
#	a=[-80, -113, -93, 53, -178, -148, -27, 9, -20, 30]
	
	start=time.clock()
	print (maxSumZero(a))
	elapsed=(time.clock()-start)
	print elapsed
	
	start=time.clock()
	print (maxSumOne(a))
	elapsed=(time.clock()-start)
	print elapsed
	
	start=time.clock()
	print (maxSumTwo(a))
	elapsed=(time.clock()-start)
	print elapsed
	
	start=time.clock()
	print (maxSumThree(a,0,len(a)-1))
	elapsed=(time.clock()-start)
	print elapsed
	
	start=time.clock()
	print (maxSumFour(a))
	elapsed=(time.clock()-start)
	print elapsed