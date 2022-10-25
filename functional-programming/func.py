"""
File: func.py

Description: map-reduce functional programming
"""
from collections import Counter


def is_palindrome(word):
    """
        Python way of checking
    """
    return word == word[::-1]


def is_palindrome_iterative(word):
    pos = 0
    while pos < len(word)/2:
        if word[pos] != word[len(word)-pos-1]:
            return False
        pos += 1
    return True


def is_palindrome_functional(word):
    """
        Functional programming palindrome -- avoid loops, pointers
    """
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_functional(word[1:-1])


def palandromic(letters):
    return sum(map(lambda x: x % 2, Counter(letters).values())) <=1


def main():
    word = 'racecar'
    print(is_palindrome(word))
    print(is_palindrome_iterative(word))
    print(is_palindrome_functional(word))
    print(palandromic(word))


if __name__ == '__main__':
    main()
