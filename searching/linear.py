def linear_search(arr: list, x: int):
    """
    Perform a linear search to find the element in the list.

    Args:
        arr (list): The list to search through.
        x (int): The element to search for.

    Returns:
        int: The element if found, otherwise -1.

    Example:
        >>> arr = [1, 2, 3, 4, 5, 6]
        >>> linear_search(arr, 2)
        2

    Time Complexity:
        O(n), where n is the number of elements in the list. In the worst case,
        the algorithm will have to check all elements.

    Space Complexity:
        O(1). The algorithm uses a constant amount of extra space regardless
        of the size of the input list.
    """
    for item in arr:
        if x == item:
            return x
    return -1


arr = [1, 2, 3, 4, 5, 6]
print(linear_search(arr, 2))
