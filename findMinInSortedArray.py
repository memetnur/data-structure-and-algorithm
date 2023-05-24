"""
The time complexity of this binary search approach is O(log(N)), where N is the number of elements in the input array. At each step, the search space is divided in half, leading to a logarithmic time complexity.

The space complexity is O(1) because the function only uses a constant amount of additional space to store the left, right, and mid pointers.
"""

def findMinInSortedArray(array):
    left = 0
    right = len(array) - 1

    while left < right:
        mid = left + (right - left) // 2

        if array[mid] > array[right]:
            left = mid + 1
        else:
            right = mid

    return array[left]


print(findMinInSortedArray([3, 4, 5, 1, 2]))
