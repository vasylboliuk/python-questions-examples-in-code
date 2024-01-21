

class DictComprehension:

    @staticmethod
    def simple_dict_assignment_from_list():
        """
        Create dictionary for list with id, start from id=1
        :return:
        """
        fruits_list = ["apple", "pineapple", "mango", "lemon", "cherry"]
        result_dict = {}
        for i, value in enumerate(fruits_list):
            result_dict[i+1] = value
        return result_dict

    @staticmethod
    def dict_comprehension():
        """
        Create dictionary for list with id, using comprehension dictionary
        :return:
        """
        fruits_list = ["apple", "pineapple", "mango", "lemon", "cherry"]
        return { i+1:value for i, value in enumerate(fruits_list)}



if __name__ == '__main__':
    print(DictComprehension.simple_dict_assignment_from_list())
    print(DictComprehension.dict_comprehension())



