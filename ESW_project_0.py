def conversation():
    print("This program will subtract two numbers.")
def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            print(f"{user_input} is a good number")
            return int(user_input)
        else:
            print("Invalid Number, Try again!!!")
def main():
    conversation()
    stop_loop = "no"
    while stop_loop != "yes":
        num1 = get_valid_number("Enter first number: ")
        num2 = get_valid_number("Enter second number: ")
        print("Let's do some subtraction!")
        total = num1 - num2
        print(f"{num1} - {num2} = {total}")
        stop_loop = input("Type 'yes' to exit program: ").lower().strip()
    print()
    print("Goodbye!!!")
    print()
    print("Come back when you have more numbers:)")
if __name__ == "__main__":
    main()
