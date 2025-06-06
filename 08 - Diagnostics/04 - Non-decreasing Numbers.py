def main():
    print("Enter a sequence of non-decreasing numbers.")
    
    previous = float(input("Enter num: "))
    count = 1

    while True:
        current = float(input("Enter num: "))
        if current < previous:
            break
        count += 1
        previous = current

    print("Thanks for playing!")
    print("Sequence length:", count)

if __name__ == "__main__":
    main()
