def call_gpt(prompt):
    # Fake GPT response for classroom/demo use
    return (
        "In the silent breeze,\n"
        "NAME explores TOPIC's light,\n"
        "Dreams unfold with grace."
        .replace("NAME", name)
        .replace("TOPIC", topic)
    )

def main():
    global name, topic
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...\n")

    prompt = (
        f"Write a haiku about '{topic}' that includes the name '{name}'. "
        "Follow the traditional haiku format (5-7-5)."
    )

    haiku = call_gpt(prompt)
    print(haiku)

if __name__ == '__main__':
    main()
