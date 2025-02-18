def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

def binary_to_hexadecimal(binary):
    return hex(int(binary, 2)).replace("0x", "").upper()

def decimal_to_hexadecimal(decimal):
    return hex(decimal).replace("0x", "").upper()

def hexadecimal_to_decimal(hexa):
    return int(hexa, 16)

def hexadecimal_to_binary(hexa):
    return bin(int(hexa, 16)).replace("0b", "")

def octal_to_decimal(octal):
    return int(octal, 8)

def decimal_to_octal(decimal):
    return oct(decimal).replace("0o", "")

def octal_to_hexadecimal(octal):
    return hex(int(octal, 8)).replace("0x", "").upper()

def main():
    while True:
        while True:
            print("\nConversion Options:")
            print("(1) Binary to Decimal")
            print("(2) Decimal to Binary")
            print("(3) Binary to Hexadecimal")
            print("(4) Decimal to Hexadecimal")
            print("(5) Hexadecimal to Decimal")
            print("(6) Hexadecimal to Binary")
            print("(7) Octal to Decimal")
            print("(8) Decimal to Octal")
            print("(9) Octal to Hexadecimal")
            print("(10) Exit")
            selection = input("\nSelect an option: ")
            try:
                if selection == "1":
                    binary = input("Enter a binary number: ")
                    print(f"Decimal: {binary_to_decimal(binary)}")
                elif selection == "2":
                    decimal = int(input("Enter a decimal number: "))
                    print(f"Binary: {decimal_to_binary(decimal)}")
                elif selection == "3":
                    binary = input("Enter a binary number: ")
                    print(f"Hexadecimal: {binary_to_hexadecimal(binary)}")
                elif selection == "4":
                    decimal = int(input("Enter a decimal number: "))
                    print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")
                elif selection == "5":
                    hexa = input("Enter a hexadecimal number: ")
                    print(f"Decimal: {hexadecimal_to_decimal(hexa)}")
                elif selection == "6":
                    hexa = input("Enter a hexadecimal number: ")
                    print(f"Binary: {hexadecimal_to_binary(hexa)}")
                elif selection == "7":
                    octal = input("Enter an octal number: ")
                    print(f"Decimal: {octal_to_decimal(octal)}")
                elif selection == "8":
                    decimal = int(input("Enter a decimal number: "))
                    print(f"Octal: {decimal_to_octal(decimal)}")
                elif selection == "9":
                    octal = input("Enter an octal number: ")
                    print(f"Hexadecimal: {octal_to_hexadecimal(octal)}")
                elif selection == "10":
                    print("Exiting program.")
                    return
                else:
                    print("Invalid selection. Please choose a valid option.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

            exit_choice = input("\nType 'yes' to end program or press Enter to continue: ").lower()
            if exit_choice == "yes":
                return

if __name__ == "__main__":
    main()
