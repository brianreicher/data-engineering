class Stack():

    def __init__(self):
        self._items = []

    def size(self):
        pass

    def __len__(self) -> int:
        return len(self._items)

    def push(self, x):
        self._items.append(x)


    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            return None

    def top(self):
        if self._items == 0:
            return None
        else:
            return self._items[-1]