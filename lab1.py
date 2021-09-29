
def main():

    a, n, d = map(float, input("Enter first term of a progression, number of term, and difference with a space: ").split())
    sum =  (2 * a + d * (n - 1)) / 2 * n
    print("The soum of a progression: ", sum)

main()
