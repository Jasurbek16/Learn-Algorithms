"""A function to find the smallest item from an array
and return its index"""

def findSmallestFunc(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for item in range(1, len(arr)):
        if smallest > arr[item]:
            smallest = arr[item]
            smallest_index = item
    return smallest_index