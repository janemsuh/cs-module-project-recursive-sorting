# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here
    # starting at the beginning of arrA and arrB
    # compare the next value of each
    # add smallest to merged_arr
    merged_arr = []
    while (len(arrA) > 0 and len(arrB) > 0):
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        else:
            merged_arr.append(arrA[0])
            arrA.pop(0)
    while len(arrA) > 0:
        merged_arr.append(arrA[0])
        arrA.pop(0)
    while len(arrB) > 0:
        merged_arr.append(arrB[0])
        arrB.pop(0)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    # if len(arr) > 1:
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces
    midpoint = len(arr) // 2
    arrA = arr[:midpoint]
    arrB = arr[midpoint:]
    return merge(merge_sort(arrA), merge_sort(arrB))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

