
def fibo(n):
	# n = int(input("please enter the no"));
	a,b=0,1
	while a<n:
		print(a)
		a,b = b, a+b
fibo(2000)