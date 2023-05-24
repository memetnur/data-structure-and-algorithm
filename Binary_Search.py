'''
The binary_search function implements the Binary Search algorithm. It takes a sorted array and a target value as input and searches for the index of the target value in the array.

Time: O(log(N)), 
where N is the number of elements in the array. This is because the search space is halved in each iteration, resulting in a logarithmic time complexity. 
Space: O(1) since the algorithm does not require additional memory apart from a few variables.
'''

def binary_search(array, target):
    """
    Perform Binary Search on the given sorted array to find the index of the target value.

    :param array: Sorted array
    :param target: Target value to search
    :return: Index of the target value, -1 if not found
    """

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if target < array[mid]:
            right = mid - 1
        elif target > array[mid]:
            left = mid + 1
        else:
            return mid

    return -1
