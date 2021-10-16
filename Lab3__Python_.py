def main():
    
    n = 0;
    deltS = 1
    s = 0
    e = 0.00001
    x = float(input("Enter x: "))
    while (abs(deltS)  > e) :
        sign = (-1)**n
        numtor = x**(2 * n) + 1
        demtor = 2**n + 1
        deltS = sign * numtor / demtor
        s = s + deltS
        n += 1
        print(n, " element: ", format(deltS, '.6f'), "  The sum: ", format(s, '.6f'))
    print("Result:", format(s, '.6f'))

main()