from math import log10
i = 5
def func(i):
    i1 = i * i
    log = int(1 + log10(i))
    biss = 10**log
    if ((i1 - i) % biss == 0) :
        print(f" {i} {i1}")

def main():
    n = int(input("Hello"))
    for i in range (5, n, 10) :
        func(i)
        i + 1
        func(i + 1)
        i - 1
main()
