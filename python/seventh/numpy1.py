import numpy as np

def main():
    # Create a sample 2D array
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    print("Original 2D Array:")
    print(arr)
    print()

    # Display array elements in reverse order
    print("Array elements in reverse order:")
    print(arr[::-1])
    print()

    # Display principal diagonal elements
    print("Principal diagonal elements:")
    print(np.diag(arr))
    print()

    # Sort the array in ascending order (default axis=None sorts flattened array)
    print("Sorted array in ascending order:")
    print(np.sort(arr, axis=None))
    print()

    # Sort the array in descending order (use slicing with ::-1)
    print("Sorted array in descending order:")
    print(np.sort(arr, axis=None)[::-1])
    print()

if __name__ == "__main__":
    main()
