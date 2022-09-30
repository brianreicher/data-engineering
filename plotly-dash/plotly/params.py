# *args & **kwargs
def args_kwargs_func(*args, **kwargs):
    print(f'Given args: {type(args)}. {args}')
    print(f'Given kwargs: {type(kwargs)}, {kwargs}')
    print(sum(args))


if __name__ == "__main__":
    args_kwargs_func(5, 6, 7, 8, 9, 10, a="hello", b=52, c=True)
