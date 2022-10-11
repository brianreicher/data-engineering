from typing import List, Dict, Tuple


# dynamic typing
def add(x, y):
    return x+y


# type hints

def multiply(x: int, y: int) -> int:
    return x*y


l: List[int] = [1, 2, 3, 4]


def main():
    print(add(2, 4))


main()
