

class Stack:
    def __init__(self):
        self._size = 50
        self._arr = [0] * self._size
        self._count = 0

    def __len__(self):
        return self._count

    def __str__(self):
        result = "["

        for i in range(len(self)):
            if i > 0:
                result += ", "
            result += str(self._arr[i])
        result += "]"

        return result

    def push(self, value) -> None:
        self._arr[self._count] = value
        self._count += 1

    def pop(self):
        value = self._arr[self._count-1]
        self._count -= 1
        return value

    def peek(self):
        value = self._arr[self._count-1]
        return value

    