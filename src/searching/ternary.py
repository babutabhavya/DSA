from typing import Any
from base import Search


class TernarySearch(Search):
    """
    TernarySearch extends the Search class to implement the ternary search algorithm.

    Ternary search divides the sorted array into three parts and narrows down the search space
    based on comparisons with two midpoints, mid1 and mid2.

    Attributes:
        arr (List[Any]): The list of elements to search, inherited from the base Search class.
    """

    def search(self, x: Any) -> int:
        """
        Perform ternary search to find the target element x in the sorted list arr.

        Args:
            x (Any): The element to search for.

        Returns:
            int: The index of the target element if found, otherwise -1.
        """
        low = 0
        high = len(self.arr) - 1

        while high >= low:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3

            if x == self.arr[mid1]:
                return mid1
            if x == self.arr[mid2]:
                return mid2
            if x < self.arr[mid1]:
                high = mid1 - 1
            elif x > self.arr[mid2]:
                low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1

        return -1


obj = TernarySearch([1, 2, 3, 4, 5])
print(f"Item found at index: {obj.search(5)}")
