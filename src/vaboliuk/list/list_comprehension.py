import random


class ListComprehension:
    """
    Task-1: Given the random list with elements need to create new list with odd numbers
    Task-2: Given the random list with elements need to create new list with fixed size with odd numbers
    """

    @staticmethod
    def simple_list_conversion():
        print("simple_list_conversion")
        random_list = []
        for i in range(0, 20):
            random_list.append(random.randint(0, 20))
        list_result = []
        print(f"Input List: {random_list}")
        for i in random_list:
            if i % 2 != 0:
                list_result.append(i)
        print(f"Output List: {list_result}")
        return list_result

    @staticmethod
    def comprehension_list():
        print("comprehension_list")
        random_list = [random.randint(0, 20) for i in range(0, 20)]
        print(f"Input List: {random_list}")
        list_result = [ i for i in random_list if i % 2 != 0 ]
        print(f"Output List: {list_result}")

    @staticmethod
    def comprehension_list_in_one_line():
        print("comprehension_list_in_one_line")
        result_list = [i for i in [random.randint(0, 20) for i in range(0, 20)] if i % 2 != 0]
        print(f"Output List: {result_list}")
        return result_list

    @staticmethod
    def simple_list_task_2_generate_fixed_size_list_with_odd_numbers():
        print("simple_list_task_2_generate_fixed_size_list_with_odd_numbers")
        list_size = 10
        list_result = []
        while len(list_result) != list_size:
            random_number = random.randint(0, 20)
            if random_number % 2 != 0:
                list_result.append(random_number)
        print(f"Output List: {list_result}")



if __name__ == '__main__':
    ListComprehension.simple_list_conversion()
    ListComprehension.comprehension_list()
    ListComprehension.comprehension_list_in_one_line()
    ListComprehension.simple_list_task_2_generate_fixed_size_list_with_odd_numbers()


