from typing import Any
from base import Search


class BinarySearch(Search):
    """
    A Binary Search implementation inheriting from the Search base class.

    This class provides a method to perform binary search on a sorted list.
    """

    def search(self, x: Any):
        """
        Perform a binary search to find the element in the sorted list.

        Args:
            x (Any): The element to search for.

        Returns:
            Any: The index of the element if found, otherwise -1.

        Example:
            >>> arr = [1, 2, 3, 4, 5, 6, 7]
            >>> search_instance = BinarySearch(arr)
            >>> search_instance.search(5)
            5

        Time Complexity:
            O(log n), where n is the number of elements in the list. The algorithm
            repeatedly divides the search interval in half.

        Space Complexity:
            O(1). The algorithm uses a constant amount of extra space regardless
            of the size of the input list.
        """
        high = len(self.arr) - 1
        low = 0

        while high >= low:
            mid = (high + low) // 2
            if x == self.arr[mid]:
                return mid
            elif x > self.arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1


obj = BinarySearch([1, 2, 3, 4, 5, 6])
print(f"Found at index: {obj.search(5)}")
