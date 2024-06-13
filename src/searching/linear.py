from typing import Any
from base import Search


class LinearSearch(Search):
    """Linear search algorithm implementation.

    This class performs a linear search to find the target element
    in the list provided during initialization.
    """

    def search(self, x: Any) -> int:
        """Search for the target element in the list using linear search.

        Args:
            x (Any): The element to search for.

        Returns:
            int: The index of the target element if found, otherwise -1.
        """
        for index, item in enumerate(self.arr):
            if x == item:
                return index
        return -1


obj = LinearSearch([1, 2, 3, 4, 5, 6])
print(f"Item found at index: {obj.search(3)}")
