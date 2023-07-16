list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.len_list = len(self.list_of_list)

    def __iter__(self):
        self.inter_index = -1
        self.exter_index = 0
        return self

    def __next__(self):
        self.inter_index += 1
        if self.inter_index >= len(self.list_of_list[self.exter_index]):
            self.exter_index += 1
            self.inter_index = 0
        if self.exter_index >= self.len_list:
            raise StopIteration

        return self.list_of_list[self.exter_index][self.inter_index]

def print_item(iter_object):
    for i in iter_object:
        print(i)

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
    flat_iter = FlatIterator(list_of_lists_1)
    print_item(flat_iter)
