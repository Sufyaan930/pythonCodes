def show_menu():
    print("\n===== Simple Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        return "❌ Error! Division by zero."
    return num1 / num2

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1,num2)
        elif choice == "2":
            result = subtract(num1,num2)
        elif choice == "3":
            result = multiply(num1,num2)
        elif choice == "4":
            result = divide(num1,num2)

            print(f"Result: {result}")
        elif choice =="5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose 1-5.")
if __name__ == "__main__":
    main()