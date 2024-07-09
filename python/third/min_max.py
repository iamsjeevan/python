def find_max_min(arr):
    if not arr:
        return None, None
    max_num = arr[0]
    min_num = arr[0]
    for num in arr[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

def main():
    # Example array
    arr = [12, 35, 1, 10, 34, 1]
    
    # Display the maximum and minimum number from the array
    max_num, min_num = find_max_min(arr)
    print(f"Maximum number: {max_num}")
    print(f"Minimum number: {min_num}")
    
    # Display the second largest number from the array without sorting
    second_largest = find_second_largest(arr)
    print(f"Second largest number: {second_largest}")

if __name__ == "__main__":
    main()
