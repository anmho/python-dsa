

def Dict():
    def __init__(self):
        pass

    def __getitem__(self):
        pass

    def __get__(self, i: int):
        return self.arr[i]


a = Dict()
print(a[0])
