from math import sqrt

def main():
    a, b = map(float, input("Enter a and b ").split())
    x1 = root(root(a))
    x2 = sqrt(root(b))
    x3 = root(a+b)
    Y = x1 + x2 + x3
    print("Y = "Y)

def root(x):
    Z0 = x 
    z = Z0
    eps = 0.00001
    while True:
        Z0 = z
        l = x / (Z0 * Z0)
        z = 1.0 / 3.0 * (l + 2 * Z0)
        if (abs(Z0 - z) < eps): 
            break
       
    return z

main()
