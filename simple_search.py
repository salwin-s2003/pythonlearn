def linear_search(arr, target):
    """
    Perform a linear search for the target in the list.
    Returns the index of the target if found, else -1.
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    """
    Perform a binary search for the target in a sorted list.
    Returns the index of the target if found, else -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    sample_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 7

    print("Linear Search:")
    index = linear_search(sample_list, target_value)
    if index != -1:
        print(f"Found {target_value} at index {index}")
    else:
        print(f"{target_value} not found in the list")

    print("\nBinary Search:")
    index = binary_search(sample_list, target_value)
    if index != -1:
        print(f"Found {target_value} at index {index}")
    else:
        print(f"{target_value} not found in the list")
