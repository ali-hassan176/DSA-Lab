import ctypes

class Aseq:
    def __init__(self):
        self._capacity = 4
        self._A = (self._capacity * ctypes.py_object)()
        for i in range(self._capacity):
            self._A[i] = None
        self._size = 0
        self._front = 0
        self._back = -1

    def _resize(self, new_capacity):
        B = (new_capacity * ctypes.py_object)()
        for i in range(self._size):
            B[i] = self._A[(self._front + i) % self._capacity]
        self._A = B
        self._capacity = new_capacity
        self._front = 0
        self._back = self._size - 1

    def insert_first(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._front = (self._front - 1) % self._capacity
        self._A[self._front] = value
        if self._size == 0:
            self._back = self._front
        self._size += 1

    def insert_last(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._back = (self._back + 1) % self._capacity
        self._A[self._back] = value
        if self._size == 0:
            self._front = self._back
        self._size += 1

    def get_at(self, i):
        if i < 0 or i >= self._size:
            return None
        return self._A[(self._front + i) % self._capacity]

    def is_empty(self):
        return self._size == 0

    def length(self):
        return self._size

    def toList(self):
        L = []
        for i in range(self._size):
            L.append(self._A[(self._front + i) % self._capacity])
        return L

    def insert_at(self, index, value):
        if index < 0 or index > self._size:
            return
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        if index < self._size // 2:
            self._front = (self._front - 1) % self._capacity
            for i in range(index):
                self._A[(self._front + i) % self._capacity] = self._A[(self._front + i + 1) % self._capacity]
        else:
            self._back = (self._back + 1) % self._capacity
            for i in range(self._size - 1, index - 1, -1):
                self._A[(self._front + i + 1) % self._capacity] = self._A[(self._front + i) % self._capacity]
        self._A[(self._front + index) % self._capacity] = value
        self._size += 1

    def delete_at(self, index):
        if index < 0 or index >= self._size:
            return
        for i in range(index, self._size - 1):
            self._A[(self._front + i) % self._capacity] = self._A[(self._front + i + 1) % self._capacity]
        self._A[self._back] = None
        self._back = (self._back - 1) % self._capacity
        self._size -= 1
        if 0 < self._size < self._capacity // 4:
            self._resize(self._capacity // 2)

# Test code
if __name__ == "__main__":
    a = Aseq()
    a.insert_last(5)
    a.insert_last(10)
    a.insert_first(15)
    print(a.toList())
    a.insert_at(1, 20)
    print(a.toList())
    a.delete_at(2)
    print(a.toList())
    print("Length:", a.length())
    print("Is Empty:", a.is_empty())
    print("Element at 1:", a.get_at(1))
