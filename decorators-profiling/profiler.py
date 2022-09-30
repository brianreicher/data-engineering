"""
File: profiler.py

Description: code profiler, built in Python3
"""

import time


class FunctionTimer:

    def __init__(self):
        pass

    @timer
    @staticmethod
    def squares(n: int) -> list:
        """
            Function to compute squares of all integers up to a given value

            :param n: int:
                Integer, n, to perform squaring operations on
            :return:
                List of squared values from 0-n
        """
        return [i**2 for i in range(n)]

    @staticmethod
    def timer(f):
        """
            Decorator for calculating function result & runtime
        :param f:
            Given function to evaluate
        :return:
            Elapsed function compute time, function result
        """
        def wrapper(*args, **kwargs):
            start = time.time()
            val = f(*args, **kwargs)
            end = time.time()
            elapsed_time = end - start
            return elapsed_time, val

        return wrapper


def main():
#     print(squares(10000000))
    pass


if __name__ == '__main__':
    main()


