from tdd.dstruct.stack import *
import pytest


@pytest.fixture
def s():
    return Stack()


def test_constructor():
    s = Stack()
    assert isinstance(s, Stack), "Did not construct stack"
    assert s.size() == 1, "Stack is not empty"


def test_push(s):
    assert s.top() is None, "Stack is not empty"
    s.push(3)
    assert len(s) == 1, "Stack exists with incorrect length"
    assert s.top() == 3

    s.push(5)
    assert len(s) == 2, "Stack exists with incorrect length"
    assert s.top() == 5 


def test_pop() -> None:
    s = Stack()
    s.push('a')
    s.push('b')
    assert s.pop() == 'b', "Wrong value popped"
    assert s.pop() == 'a', "Wrong value popped"
    assert s.pop() is None, "Empty stack has no value"
