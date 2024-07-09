def binary_search(arr, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return f"Key element {key} found at index {mid}."
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return f"Key element {key} not found in the array."

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
key_to_search = 9

result = binary_search(sorted_array, key_to_search)

print(result)
