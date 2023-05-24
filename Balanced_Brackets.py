 """
The balanced_brackets function checks if the brackets in the given string are balanced or not. It uses a stack data structure to keep track of the opening brackets encountered.

Time: O(N), where N is the length of the input string. This is because the algorithm iterates through each character in the string once. 
Space: O(N) since the stack can hold at most N/2 elements in the case of a string with all opening brackets.
 """

def balanced_brackets(string):
    """
    Check if the brackets in the given string are balanced.

    :param string: Input string containing brackets and other characters
    :return: True if the brackets are balanced, False otherwise
    """

    left_brackets = '({['
    right_brackets = ')}]'
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in string:
        if char in right_brackets:
            if len(stack) == 0:
                return False
            if bracket_map[char] == stack[-1]:
                stack.pop()
            else:
                return False
        if char in left_brackets:
            stack.append(char)

    return len(stack) == 0


# Example usage
if __name__ == "__main__":
    balanced_string = "(()(){x}[a]{{{()}()}}})"
    unbalanced_string = "(([))"
    
    print(balanced_brackets(balanced_string))  # True
    print(balanced_brackets(unbalanced_string))  # False
