def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Unsupported operation - check the types of operands.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"The result of {a} divided by {b} is {result:.2f}")
    finally:
        print("Execution of divide_numbers function completed.")

def main():
    # Test cases
    divide_numbers(10, 2)  # No exceptions
    divide_numbers(10, 0)  # ZeroDivisionError
    divide_numbers(10, '2')  # TypeError

if __name__ == "__main__":
    main()
