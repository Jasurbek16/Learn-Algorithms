"""A function that performs the binary search for a given array of elements"""

def binarySearchFunc(list_of_elements, target_element):
    
    low = 0
    high = len(list_of_elements) - 1

    while low <= high:
        
        mid = (low + high) // 2
        guess = list_of_elements[mid]
        if guess == target_element:
            return mid
        if guess < target_element:
            low = mid + 1
        else:
            high = mid - 1
    return "The element not found"

my_list = [1, 2, 5, 6, 8, 9]

print(binarySearchFunc(my_list, 5))
print(binarySearchFunc(my_list, -4))




