def main():
    print("Welcome to the Simple Adder!")
    
    # Ask the user for two numbers
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Convert the input strings to numbers
    num1 = float(num1)
    num2 = float(num2)

    # Add the numbers
    result = num1 + num2

    # Show the result
    print("The sum is:", result)

if __name__ == '__main__':
    main()
