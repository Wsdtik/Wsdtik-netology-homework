class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.outer = 0
        self.inner = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.outer >= len(self.list_of_lists):
            raise StopIteration
        if self.inner >= len(self.list_of_lists[self.outer]):
            self.outer += 1
            self.inner = 0
            return self.__next__()
        item = self.list_of_lists[self.outer][self.inner]
        self.inner += 1
        return item

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()
