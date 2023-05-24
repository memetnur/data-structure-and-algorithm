"""
Time: O(N log N), where N is the number of nodes in the linked list. This is because the list is recursively divided into halves, and each merge operation takes linear time.

Space: O(log N) due to the recursive calls in the merge sort algorithm.
"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def sort(linkedList):
    if linkedList is None or linkedList.next is None:
        return linkedList
    
    # Split the linked list into two halves
    middle = getMiddle(linkedList)
    secondHalf = middle.next
    middle.next = None
    
    # Recursively sort the two halves
    sortedFirstHalf = sort(linkedList)
    sortedSecondHalf = sort(secondHalf)
    
    # Merge the sorted halves
    sortedList = merge(sortedFirstHalf, sortedSecondHalf)
    return sortedList

def getMiddle(head):
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(left, right):
    dummy = LinkedList(0)
    current = dummy
    
    while left and right:
        if left.value < right.value:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    
    if left:
        current.next = left
    elif right:
        current.next = right
    
    return dummy.next

# Build a LinkedList
linkedList = LinkedList(10)
nextNode = linkedList
for i in reversed(range(10)):
    nextNode.next = LinkedList(i)
    nextNode = nextNode.next

print("Before sorting:")
current = linkedList
while current is not None:
    print(current.value, end=" ")
    current = current.next
print()

sortedList = sort(linkedList)

print("After sorting:")
current = sortedList
while current is not None:
    print(current.value, end=" ")
    current = current.next
print()
