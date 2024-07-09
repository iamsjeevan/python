import random

def generate_random_numbers(count):
    return [random.randint(1, 100) for _ in range(count)]

def filter_odd_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers

def filter_length(numbers):
    filtered_numbers = [num for num in numbers if len(str(num)) in (2, 4)]
    return filtered_numbers

def main():
    # Generate 20 random numbers
    random_numbers = generate_random_numbers(20)
    print("Generated random numbers:")
    print(random_numbers)
    
    # Filter odd numbers of length 2 or 4
    odd_numbers = filter_odd_numbers(random_numbers)
    filtered_numbers = filter_length(odd_numbers)
    
    # Display filtered numbers
    print("\nOdd numbers of length 2 or 4:")
    print(filtered_numbers)

if __name__ == "__main__":
    main()
