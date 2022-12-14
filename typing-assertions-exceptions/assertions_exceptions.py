import traceback


def add(x, y) -> int:
    assert type(x) in [int, float] and type(y) in [int, float], 'Non numeric inputs'
    assert x > 0 and y > 0, 'negative values not allowed'

    return x + y


def ex_funct():
    func_list = range(1, 6)
    print(func_list[99])


def main():
    try:
        a = add(2, 2)
        b = add('hello', 'world')
        print(a, b)
    # except Exception as e:
    except AssertionError as e:
        print(str(e))

    try:
        ex_funct()
    except Exception as e:
        print(str(e))
        # printing actual traceback
        traceback.print_exception(e)


if __name__ == '__main__':
    main()
