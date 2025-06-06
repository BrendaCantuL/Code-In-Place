import random

NUM_PAIRS = 3

def clear_terminal():
    print()  # ✅ safe in all environments

def create_truth_list(num_pairs):
    truth = []
    for i in range(num_pairs):
        truth.append(i)
        truth.append(i)
    return truth

def get_valid_index(displayed, prompt, exclude_index=None):
    while True:
        index_input = input(prompt)

        if not index_input.isdigit():
            print("Not a number. Try again.")
            continue

        index = int(index_input)

        if index < 0 or index >= len(displayed):
            print("Invalid index. Try again.")
            continue

        if displayed[index] != '*':
            print("This number has already been matched. Try again.")
            continue

        if exclude_index is not None and index == exclude_index:
            print("You entered the same index twice. Try again.")
            continue

        return index

def display_board(displayed):
    print(displayed)

def main():
    truth = create_truth_list(NUM_PAIRS)
    random.shuffle(truth)

    displayed = ['*'] * len(truth)

    while '*' in displayed:
        display_board(displayed)

        index1 = get_valid_index(displayed, "Enter an index: ")
        index2 = get_valid_index(displayed, "Enter an index: ", exclude_index=index1)

        if truth[index1] == truth[index2]:
            displayed[index1] = truth[index1]
            displayed[index2] = truth[index2]
            print("Match!")
            clear_terminal()
        else:
            print(f"Value at index {index1} is {truth[index1]}")
            print(f"Value at index {index2} is {truth[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")  # wait for enter
            clear_terminal()

    display_board(displayed)
    print("Congratulations! You won!")

if __name__ == '__main__':
    main()
