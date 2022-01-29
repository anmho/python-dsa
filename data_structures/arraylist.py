
class ArrayList:
    def __init__(self):
        self.size = 5
        self.arr = [0 for i in range(self.size)]
        self.count = 0

    def add_front(self, value):
        if len(self) + 1 > self.size:
            self.__resize__()

        for i in range(len(self)-1, -1, -1):
            self.arr[i+1] = self.arr[i]
        self.size += 1

    def add(self, value):  # adds value to end of list
        # resize if necessary
        if self.count + 1 > self.size:
            self.__resize__()
        self.arr[self.count] = value
        self.count += 1

    def __resize__(self):
        new_size = int(self.size * 2)
        new_arr = [0 for i in range(new_size)]
        # copy over elements
        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.size = new_size

    def insert(self, value, index):
        # resize if necessary
        if self.count + 1 > self.size:
            self.__resize__()

        # shift values forward if necessary
        if index <= 0:
            for i in range(len(self)-1, -1, -1):
                self.arr[i+1] = self.arr[i]
            self.arr[0] = value
            self.count += 1
        elif index >= len(self) - 1:  # insert at end if > len
            self.arr[len(self)]
            self.count += 1
        else:
            for i in range(len(self)-1, index-1, -1):
                self.arr[i+1] = self.arr[i]
            self.arr[index] = value
            self.count += 1

    def __len__(self):
        return self.count

    def print(self):
        print("[", end="")
        for i in range(self.count):
            if i > 0:
                print(", ", end="")
            print(self.arr[i], end="")
        print("]")

    def __str__(self):
        result = "["
        for i in range(self.count):
            if i > 0:
                result += ", "
            result += str(self.arr[i])

        result += "]"
        return result

    def remove(self, index):
        for i in range(index, len(self)-1):
            self.arr[i] = self.arr[i+1]
        self.count -= 1

    def __getitem__(self, index):
        return self.arr[index]
