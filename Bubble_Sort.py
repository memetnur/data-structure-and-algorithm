'''
The bubble_sort function implements the Bubble Sort algorithm. 
It takes an unsorted array as input and repeatedly iterates through the array, comparing adjacent elements and swapping them if they are in the wrong order. This process is repeated until the entire array is sorted.

The algorithm works by using a boolean variable is_sorted to keep track of whether any swaps were made during a pass through the array. If no swaps are made in a pass, it means the array is already sorted, and the algorithm terminates. The index variable is used to optimize the sorting process by reducing the number of elements to consider in each pass, as the largest elements gradually "bubble up" to their correct positions.

The swap function is a helper function used to swap two elements in the array. It takes the array and the indices of the two elements to be swapped and performs the swap.

Time: O(N^2), where N is the number of elements in the array. 
Time best: O(N), when the array is already sorted.
Space: O(1) since the sorting is done in-place without requiring additional memory.

'''

def bubble_sort(array):
    """
    Perform Bubble Sort on the given unsorted array and return the sorted array.

    :param array: Unsorted array
    :return: Sorted array
    """

    is_sorted = False
    index = 0

    while not is_sorted:
        is_sorted = True

        for i in range(1, len(array) - index):
            if array[i] < array[i - 1]:
                swap(array, i, i - 1)
                is_sorted = False

        index += 1

    return array


def swap(array, left, right):
    """
    Swap two elements in the given array.

    :param array: Array
    :param left: Index of the first element
    :param right: Index of the second element
    """

    array[left], array[right] = array[right], array[left]
