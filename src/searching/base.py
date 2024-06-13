from abc import ABC, abstractmethod
from typing import List, Any


class Search(ABC):
    """
    An abstract base class for search algorithms.

    This class provides a template for search algorithms, requiring them to implement
    the search method. It stores the list to be searched as an instance variable.

    Attributes:
        arr (List): The list of elements to be searched.
    """

    def __init__(self, arr: List) -> None:
        """
        Initialize the Search class with a list of elements.

        Args:
            arr (List): The list of elements to be searched.
        """
        super().__init__()
        self.arr = arr

    @abstractmethod
    def search(self, x: Any):
        """
        Abstract method to search for an element in the list.

        This method must be implemented by any subclass of Search.

        Args:
            x (Any): The element to search for.

        Returns:
            Any: The result of the search, which will be defined by the subclass implementation.
        """
        pass
