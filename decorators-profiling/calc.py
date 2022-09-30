"""
File: calc.py

Description: OOD review
"""


class Calculator:

    def __init__(self, name: str):
        """
            Constructor
            :param name:
                The name of the calculator instance
        """
        self.name = name

    def add(self, x, y):
        """Method to perform addition"""
        print(f'{self.name} is thinking')
        return x+y


def main():
    c1 = Calculator('HP 41CV')
    c2 = Calculator('TI84 CE')

    print(c1.add(5, 10), c2.add(10, 20))


if __name__ == '__main__':
    main()
