"""
The time complexity of this algorithm is O(N), where N is the number of nodes in the linked list. It iterates through each node once to check for duplicates and update the references.

The space complexity is O(1) because the algorithm uses a constant amount of additional space to store the visited set and the references to the current and previous nodes.
"""

class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

def removeDuplicatesFromLinkedList(linkedList):
	visited = set()
	currentNode = linkedList
	prevNode = None

	while currentNode is not None:
		if currentNode.value in visited:
			prevNode.next = currentNode.next
		else:
			visited.add(currentNode.value)
			prevNode = currentNode
		currentNode = currentNode.next

	return linkedList
