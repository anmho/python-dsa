
from asyncio import InvalidStateError

# shifts elements
class ArrayQueue:
    def __init__(self, size) -> None:
        self.arr = [0] * size
        self.capacity = size
        self.front = 0
        self.rear = 0
        self.count = 0

    def __len__(self):
        return self.count

    def __str__(self):
        result = "["

        for i in range(self.front, self.rear):
            if i > self.front:
                result += ", "
            result += str(self.arr[i])

        result += "]"
        return result

    def enqueue(self, value):
        if self.count == self.capacity:
            raise InvalidStateError()

        if self.rear == self.capacity and self.count < self.capacity:
            k = 0
            for i in range(self.front, self.rear):
                self.arr[k] = self.arr[i]
                k += 1
            self.front = 0
            self.rear = self.count

        self.arr[self.rear] = value
        self.rear += 1
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise InvalidStateError()

        print(self.count, self.front, self.rear)
        value = self.arr[self.front]
        self.front += 1
        self.count -= 1
        return value

    def peek(self):
        value = self.arr[self.front]

    def isEmpty(self):
        return self.count == 0

# circular ArrayQueue
class Queue:
    