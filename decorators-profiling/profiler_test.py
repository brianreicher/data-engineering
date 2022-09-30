from profiler import Profiler, profile


@profile
def squares(n: int) -> list:
    """
        Function to compute squares of all integers up to a given value

        :param n: int:
            Integer, n, to perform squaring operations on
        :return:
            List of squared values from 0-n
    """
    return [i ** 2 for i in range(n)]


def main():
    sq = squares(100000)
    sq2 = squares(1000000)

    Profiler.report()


if __name__ == '__main__':
    main()
