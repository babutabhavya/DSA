"""
Characteristics of the Binary Search Algorithm:

1. Efficiency:
    - Time Complexity: The binary search algorithm has a time complexity of O(log n), making it highly efficient for large datasets. It significantly reduces the number of comparisons required to find an element by halving the search space in each step.
    - Space Complexity: The space complexity is O(1), meaning it requires a constant amount of extra space, which is independent of the input size. This is because it uses a few additional variables (like `low`, `high`, and `mid`) for the search process.

2. Sorted Data Requirement:
    - Precondition: Binary search requires that the input list be sorted. If the list is not sorted, the algorithm will not function correctly and may return incorrect results.

3. Divide and Conquer:
    - Methodology: Binary search employs a divide-and-conquer strategy. It repeatedly divides the search interval in half, which allows it to quickly narrow down the possible locations of the target element.

4. Deterministic:
    - Consistency: Binary search is a deterministic algorithm, meaning it will produce the same output for a given input every time it runs. There is no randomness involved in its execution.

5. Iterative Process:
    - Implementation: The given implementation of binary search is iterative, using a loop to repeatedly narrow down the search range. There are also recursive implementations of binary search, which involve function calls within the function itself.

6. Performance on Large Datasets:
    - Scalability: Due to its logarithmic time complexity, binary search performs very well on large datasets. As the size of the input grows, the number of comparisons grows much more slowly compared to linear search.

7. Comparison-Based:
    - Operation: Binary search is a comparison-based algorithm. It compares the target value to the middle element of the list to decide whether to search in the left half or the right half.
"""

import math


def binary_search(arr: list, x: int):
    """
    Perform a binary search to find the element in the sorted list.

    Args:
        arr (list): The sorted list to search through.
        x (int): The element to search for.

    Returns:
        int: The element if found, otherwise -1.

    Example:
        >>> arr = [1, 2, 3, 4, 5, 6, 7]
        >>> binary_search(arr, 5)
        5

    Time Complexity:
        O(log n), where n is the number of elements in the list. The algorithm
        repeatedly divides the search interval in half.

    Space Complexity:
        O(1). The algorithm uses a constant amount of extra space regardless
        of the size of the input list.
    """
    high = len(arr) - 1
    low = 0

    while high >= low:
        mid = (high + low) // 2
        if x == arr[mid]:
            return x
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(arr, 5))  # Output: 5
