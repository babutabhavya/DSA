from binary import BinarySearch
from linear import LinearSearch


class SearchingFactory:
    _searching_classes = {"BINARY_SEARCH": BinarySearch, "LINEAR_SEARCH": LinearSearch}

    @staticmethod
    def get_obj(name: str):
        if name not in SearchingFactory._searching_classes:
            raise NotImplementedError("This searching method not found")
        return SearchingFactory._searching_classes[name]
