def sort(str):
    lst = str.split()
    lst.sort(key = len)
    return(lst)

def main():
    str = input("Input string: ")
    print(sort(str))

main()