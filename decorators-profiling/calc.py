"""
File: calc.py

Description: OOD review
"""


class Calculator:

    def __init__(self, name: str):
        """
            Constructor method

            :param name: str:
                The name of the calculator instance
        """
        self._name = name

    def add(self, x: int, y: int):
        """
            Method to perform addition

            :param x: int
                First integer to add
            :param y: int
                Second integer to add
        """
        print(f'{self.get_name()} is thinking . . .')
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


if __name__ == '__main__':
    main()
