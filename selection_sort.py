"""A code for performing the selection sort for a given array of items"""

from find_smallest_item import findSmallestFunc

def selectionSortFunc(arr):
    new_arr = list()
    for item in range(len(arr)):
        smallest = findSmallestFunc(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selectionSortFunc([4, 7, 9, 2, 1, 5, 8]))