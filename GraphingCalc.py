import matplotlib.pyplot as plt
import numpy as np

print("Please enter your function as coeffiecients separated by spaces")
print("i.e. 1 + 2x -3x^2 would be equivalent to '1 2 -3'")
print("Press enter nothing (i.e '') to finish input")

def to_func(lst):
	def func(x):
		total, exp = 0, 0
		copy = lst[:]
		while copy:
			total += copy.pop(0) * pow(x, exp)
			exp += 1
		return total
	return func


def outputs(f, inputs):
	rV = []
	for x in inputs:
		rV.append(f(x))
	return rV

def limit(f, x, s=0, t=0.0001):
	if (abs(f(s)-f((x+s)/2)) <= t):
		return f((x+s)/2)
	else:
		return limit(f, x, (x+s)/2, t)


def dydx(f):
	if round(f(0) - f(1000))== 0:
		return lambda x: 0
	return lambda x: limit(lambda y: (f(x)-f(y))/(x-y), 0, 0.0001)

x = list(np.linspace(-10, 10, 100000))
ask = 1
coef = []
while True:
	c = input("Coef " + str(ask) + ": ")
	if c == '':
		break
	coef.append(int(c))
	ask += 1



""" Function Plot"""
f = to_func(coef)
y = outputs(f, x)
plt.subplot(2,1,1)
plt.plot(x, y)
plt.ylabel("f(x)")

""" Derivative Plot"""
f_prime = dydx(f)
yd = outputs(f_prime, x)
plt.subplot(2,1,2)
plt.plot(x, yd)
plt.xlabel("x")
plt.ylabel("f'(x)")

""" Second derivative Plot """
sec_der = dydx(f_prime)
ydd = outputs(sec_der, x)
plt.subplot(2,1,3)
plt.plot(x, ydd)
plt.xlabel("x")
plt.ylabel("f''(x)")

""" Draws plot """
plt.show()


