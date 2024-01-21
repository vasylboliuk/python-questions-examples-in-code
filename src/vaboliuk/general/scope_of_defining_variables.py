

global_var = 50

class TestScopeOfDefiningVariables:

    def calculate_numbers_compilation_error(self, param1=None, param2=None):
        """
        Global var smust be 100
        :param param1:
        :param param2:
        :return:
        """
        global_var = global_var + 50  # UnboundLocalError: local variable 'global_var' referenced before assignment
        local_var = global_var
        if param1 is None or param2 is None:
            global_var1 = 10
            return global_var1 + global_var1
        if param1 is None:
            return local_var + param1
        if param2 is None:
            return local_var + param2
        return param1 + param2

    def calculate_numbers(self, param1=None, param2=None):
        """
        Global var must be 100
        :param param1:
        :param param2:
        :return:
        """
        global global_var
        global_var = global_var + 50
        local_var = global_var
        if param1 is None or param2 is None:
            global_var1 = 10
            return global_var1 + global_var1
        if param1 is None:
            return local_var + param1
        if param2 is None:
            return local_var + param2
        return param1 + param2

    def test_calculate_numbers_compilation_error(self):
        print(self.calculate_numbers_compilation_error())

    def test_calculate_numbers(self):
        print(self.calculate_numbers())


