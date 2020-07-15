# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:
        midpoint = (start + end) // 2
        # target is in the exact middle of the array
        if arr[midpoint] == target:
            return midpoint
        # check left half
        elif arr[midpoint] > target:
            return binary_search(arr, target, start, midpoint - 1)
        # check right half
        else:
            return binary_search(arr, target, midpoint + 1, end)
    # target is not in array
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here