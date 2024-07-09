def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    while True:
        print("Enter two numbers:")
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
    
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. exit")
        choice = input("Enter choice (1/2/3/4): ")
    
    
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
            continue
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print("exiting....")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
