

class ListNewListWithItemsBackwards:
    """
    Task-1: Input data is a list with string items: fruits = ["cherry", "mango", "banana", "kiwi", "apple", "grape"].
            As a User I would like to see the same list but backwards.
    Task-2: Input data is a list with string items: fruits = ["cherry", "mango", "banana", "kiwi", "apple", "grape"].
        As a User I would like to see the same list but each item is written backwards.
    """

    _fruits = ["cherry", "mango", "banana", "kiwi", "apple", "grape"]

    def list_backwards_simple_loop(self):
        """
        Task-1: Using simple list
        """
        print("\nTask-1: list_backwards_simple_loop")
        print(f"Input List: {self._fruits}")
        output_results = []
        len_fruits = len(self._fruits)
        for i in range(0, len_fruits):
            output_results.append(self._fruits[len_fruits - 1 - i])
        print(f"Output List: {output_results}")

    def list_backwards_list_comprehension(self):
        """
        Task-1: Using list comprehension
        """
        print("\nTask-1: list_backwards_list_comprehension")
        print(f"Input List: {self._fruits}")
        len_fruits = len(self._fruits)
        output_results = [self._fruits[len_fruits - 1 - i] for i in range(0, len_fruits)]
        print(f"Output List: {output_results}")

    def list_backwards_list_reverse(self):
        """
        Task-1: Using list reverse() function
        """
        print("\nTask-1: list_backwards_list_reverse")
        print(f"Input List: {self._fruits}")
        cloned_list = [i for i in self._fruits]
        cloned_list.reverse()
        print(f"Output List: {cloned_list}")

    def list_backwards_list_slice_operator(self):
        """
        Task-1: Using list [::-1] slice operator
        """
        print("\nTask-1: list_backwards_list_slice_operator")
        print(f"Input List: {self._fruits}")
        reversed_list = self._fruits[::-1]
        print(f"Output List: {reversed_list}")

    def list_each_item_written_backwards(self):
        print("\nTask-2: list_each_item_written_backwards")
        print(f"Input List: {self._fruits}")
        output_list = [i[::-1] for i in self._fruits]
        print(f"Output List: {output_list}")


if __name__ == '__main__':
    # Task-1
    ListNewListWithItemsBackwards().list_backwards_simple_loop()
    ListNewListWithItemsBackwards().list_backwards_list_comprehension()
    ListNewListWithItemsBackwards().list_backwards_list_reverse()
    ListNewListWithItemsBackwards().list_backwards_list_slice_operator()

    # Task-2
    ListNewListWithItemsBackwards().list_each_item_written_backwards()







