

class HandleException:
    """
    Task-1: Need to use all keywords in handle error exceptions
    """

    @staticmethod
    def handle_exception_divide(x, y):
        try:
            result = x / y
            print(f"Try block: {result}")
        except ZeroDivisionError as ex:
            # raise ValueError("Invalid parameter. Division on zero")
            print("Invalid parameter. Division on zero")
        else:
            print("else block")
            print(f"else block {result}")
        finally:
            print("Finally block")


if __name__ == '__main__':
    HandleException.handle_exception_divide(10, 0)
    print("-----------------------")
    HandleException.handle_exception_divide(4, 2)