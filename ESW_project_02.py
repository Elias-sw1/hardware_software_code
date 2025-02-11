def conversation():
    print("Welcome to my conversation program")
    print()
    print("I will keep asking questions until you type 'exit'.")
    print()
def main():
    print()
    conversation()
    print("1. What is your name?")
    name = input()
    if name.lower() == "exit":
        print("\nThanks for chatting with me.")
        return
    print()
    questions = [
        "2. What is your favorite movie, {}?".format(name),
        "3. Do you like superheroes or not, {}?".format(name),
        "4. If you can go anywhere in the world, What will it be, {}?".format(name),
        "5. Favorite video game console: Xbox or Playstation, {}?".format(name),
        "6. What your favorite shoe brand, {}?".format(name),
        "7. What your favorite childhood TV show, {}?".format(name),
        "8. What your favorite streaming services, {}?".format(name),
        "9. What your favorite music genre, {}?".format(name)
        ]
    count = 0
    answer = ""
    for question in questions:
        print(question)
        answer = input()
        if answer.lower() == "exit":
            print(f"\nThanks for chatting with me, {name}.")
            print(f"You answered {count} questions.")
            return
        count += 1
    print(f"\nThanks for chatting with me, {name}.")
    print(f"You answered {count} questions.")
if __name__ == "__main__":
    main()
