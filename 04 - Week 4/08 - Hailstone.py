def main():
    n = int(input("Enter a number: "))
    while n != 1:
        if n % 2 == 0:
            new_n = int(n / 2)
            print(f"{n} is even, so I take half: {new_n}")
        else:
            new_n = int(3 * n + 1)
            print(f"{n} is odd, so I make 3n+1: {new_n}")
        n = new_n

if __name__ == '__main__':
    main()
