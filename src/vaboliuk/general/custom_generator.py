import random


class DevelopCustomGenerator:
    """
    Task-1: Create simple interator without using generator
    Task-2: Create simple generator
    """

    @staticmethod
    def simple_iterator():
        print("simple_iterator")
        result_list = []
        size = 10
        for i in range(0, size):
            result_list.append(random.Random().randint(0, 100))
        print(f"Result list: {result_list}")
        return result_list

    @staticmethod
    def simple_generator():
        print("\nsimple_generator")
        size = 10
        for i in range(0, size):
            yield random.Random().randint(0, 100)


if __name__ == '__main__':
    for x in DevelopCustomGenerator.simple_iterator():
        print(x)

    for x in DevelopCustomGenerator.simple_generator():
        print(x)