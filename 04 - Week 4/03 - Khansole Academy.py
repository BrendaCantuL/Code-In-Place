import random
MIN_VALUE = 10
MAX_VALUE = 99

def main():
    print("Khansole Academy")
    # TODO: your code here
    # Generate two random numbers
    num_1 = random.randint(MIN_VALUE,MAX_VALUE)
    num_2 = random.randint(MIN_VALUE, MAX_VALUE)

    #Add the two random numbers and place the answer in answer
    answer = int(num_1 + num_2)

    #test user by asking them for the answer
    print(f"What is {num_1} + {num_2}?")
    user_answer = int(input("Your answer: "))

    #check if user answer is correct
    if user_answer == answer:
        print("Correct!")
    else:
        print('Incorrect.')
        print(f"The expected answer is {answer}")
    
    
if __name__ == '__main__':
    main()