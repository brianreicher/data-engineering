"""
File: decorator.py

Description: a demonstration of Python3 decorators
"""


def notify(f):
    """
        A decorator that reports when a function is called

    :param f:
        Given function
    :return:
        Notifying decorator
    """

    def wrapper():
        print('Running the function')
        f()
        print('Finished running')

    # notify builds wrapper around specified function
    return wrapper


def duplicate(f):
    """
        A decorator that returns a function twice
        :param f:
            Given function
        :return:
            Duplicating decorator
    """
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        f(*args, **kwargs)

    return wrapper


@notify
@duplicate
def hello_world():
    print('Hello world')


@duplicate
@notify
def hi_mom():
    print('Hi Mom!')


@duplicate
def say_hello(name: str) -> None:
    print(f'Hello {name}!')


def main():
    hello_world()
    hi_mom()
    say_hello('Brian')


if __name__ == '__main__':
    main()
