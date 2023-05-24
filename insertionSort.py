"""
The time complexity of Insertion Sort is O(N^2), where N is the number of elements in the array. In the worst case, when the array is in reverse order, the inner while loop will execute multiple times for each element, leading to the quadratic time complexity.

The space complexity is O(1) because the algorithm only requires a constant amount of additional space to store temporary variables.
"""

def insertionSort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j >= 0 and array[j] > current:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array
