"""
File: calc.py

Description: OOD review
"""


class Calculator:

    # class variables
    allocated = 0

    def __init__(self, name: str):
        """
            Constructor method

            :param name: str:
                The name of the calculator instance
        """
        # instance variables
        self._name = name

        # class variables
        Calculator.allocated += 1

    @staticmethod
    def add(x: int, y: int):
        """
            Method to perform addition

            :param x: int
                First integer to add
            :param y: int
                Second integer to add
        """
        return x+y

    def get_name(self) -> str:
        """
            Method to get the calculator name

            :return:
                Calculator name
        """
        return self._name


def main():
    c1 = Calculator('HP 41CV')
    print(c1.add(5, 10))
    c2 = Calculator('TI84 CE')
    print(c2.add(10, 20))

    # do not need to declare instance for static methods
    print(Calculator.add(22, 12))

    print(Calculator.allocated)


if __name__ == '__main__':
    main()
