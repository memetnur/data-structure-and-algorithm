"""
Time: O(N), where N is the input number n. Since the function calculates each Fibonacci number once and stores it in the memo dictionary for future reference, subsequent calls with the same value of n will retrieve the result in constant time.
Space: O(N)because the memo dictionary stores the calculated Fibonacci numbers. The dictionary will have a maximum size of n, as each Fibonacci number from 1 to n needs to be stored.
"""

The space complexity is also O(N) because the memo dictionary stores the calculated Fibonacci numbers. The dictionary will have a maximum size of n, as each Fibonacci number from 1 to n needs to be stored.

def getNthFib(n):
    memo = {}
    return memoizationHelper(n, memo)


def memoizationHelper(n, memo):
    if n in memo:
        return memo[n]

    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = memoizationHelper(n - 1, memo) + memoizationHelper(n - 2, memo)

    return memo[n]


print(getNthFib(30))
