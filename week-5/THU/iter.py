class  Fibonacci:
    def __init__(self, count):
        self.count = count
        self.a = 0
        self.b = 1
        self.i = 0

    def __next__(self):
        if self. i >= self.count:
            raise StopIteration()

            self.i += 1
            curr = self.a
            self.a, self.b = self.a + self.b, self.a
            return curr

    def __iter__(self):
        return self

for n in Fibonacci(5):
    print(n)


class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self
