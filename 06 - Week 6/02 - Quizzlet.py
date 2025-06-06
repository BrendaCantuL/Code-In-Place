def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct = 0
    total = len(translations)

    for english, spanish in translations.items():
        # PROMPT: No space after the question mark
        answer = input(f"What is the Spanish translation for {english}?")

        if answer == spanish:
            print("That is correct!")
            correct += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {spanish}.")

        print()  # ONE blank line after the response

    print(f"You got {correct}/{total} words correct, come study again soon!")
if __name__ == "__main__":
    main()