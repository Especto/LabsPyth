from math import sqrt
def main():
	
	S = 0
	N = 10000
	n = 1

	print("Enter coefficients of functions: ")
	a1, b1, c1, a2, b2, c2 = map(float,input().split())
	a1 = a1 - a2
	b1 = b1 - b2
	c1 = c1 - c2
	discr = b1 * b1 - 4 * a1 * c1
	x1 = (-b1 - sqrt(discr)) * 0.5 / a1
	x2 = (-b1 + sqrt(discr)) * 0.5 / a1
	b = max(x1, x2)
	a = min(x1, x2)
	print(f' Find the integral of funcion y = {a1:+}(x^2){b1:+}x{c1:+}')
	h = (b - a) / N
	f_b = a1 * b * b + b1 * b + c1
	while (n < N):
		a = a + h
		f_a = a1 * a * a + b1 * a + c1
		if (n % 2 == 0) :
			S = S + 2 * f_a
		else :
			S = S + 4 * f_a
		n += 1
	S = (h / 3) * (f_a + f_b + S)
	print("Result: ", abs(S))

main()