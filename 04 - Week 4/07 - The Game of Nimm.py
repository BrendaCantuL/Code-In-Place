def main():
    """
    Nimm: Two players take turns removing 1 or 2 stones from a pile.
    The last player to take a stone loses.
    """
    stones = 20
    current_player = 1

    while stones > 0:
        print(f"There are {stones} stones left.")
        move = int(input(f"Player {current_player} would you like to remove 1 or 2 stones? "))

        while move not in [1, 2] or move > stones:
            move = int(input("Please enter 1 or 2: "))

        stones -= move
        print()

        if stones == 0:
            winner = 2 if current_player == 1 else 1
            print(f"Player {winner} wins!")
            break

        # Switch players
        current_player = 2 if current_player == 1 else 1


if __name__ == '__main__':
    main()
