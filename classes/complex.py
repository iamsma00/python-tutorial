class Complex:
	def __init__(self,realpart,imagpart):
		self.r = realpart
		self.i = imagpart

x=Complex(3.0, -4.5)
print('real part',x.r)
print('imaginary part',x.i)
