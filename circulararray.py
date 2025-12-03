class Aseq:
    def __init__(self):
        self.array = [None] * 4
        self.size = 0
        self.capacity = 4
        self.front = 0
        self.back = 0

    def insert_first(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        
        self.front = (self.front - 1) % self.capacity
        self.array[self.front] = value
        self.size += 1

    def insert_last(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        
        self.array[self.back] = value
        self.back = (self.back + 1) % self.capacity
        self.size += 1

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[(self.front + i) % self.capacity]
        
        self.array = new_array
        self.capacity = new_capacity
        self.front = 0
        self.back = self.size

    def get_at(self, i):
        if i < 0 or i >= self.size:
            return None
        actual_index = (self.front + i) % self.capacity
        return self.array[actual_index]

    def is_empty(self):
        return self.size == 0

    def length(self):
        return self.size

    def toList(self):
        result = []
        for i in range(self.size):
            result.append(self.get_at(i))
        return result

    def insert_at(self, index, item):
        if index < 0 or index > self.size:
            return
        
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        
        if index == 0:
            self.insert_first(item)
        elif index == self.size:
            self.insert_last(item)
        else:
            for i in range(self.size, index, -1):
                self.array[(self.front + i) % self.capacity] = self.array[(self.front + i - 1) % self.capacity]
            
            insert_pos = (self.front + index) % self.capacity
            self.array[insert_pos] = item
            self.size += 1
            self.back = (self.back + 1) % self.capacity

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            return None
        
        if self.size < self.capacity // 4 and self.capacity > 4:
            self._resize(self.capacity // 2)
        
        deleted_value = self.get_at(index)
        
        if index == 0:
            self.front = (self.front + 1) % self.capacity
        elif index == self.size - 1:
            self.back = (self.back - 1) % self.capacity
        else:
            for i in range(index, self.size - 1):
                current_pos = (self.front + i) % self.capacity
                next_pos = (self.front + i + 1) % self.capacity
                self.array[current_pos] = self.array[next_pos]
            self.back = (self.back - 1) % self.capacity
        
        self.size -= 1
        return deleted_value


def test_aseq():
    a = Aseq()
    
    # Test insert_last and insert_first
    a.insert_last(5)
    a.insert_last(10)
    a.insert_first(15)
    assert a.toList() == [15, 5, 10]
    
    # Test get_at
    assert a.get_at(0) == 15
    assert a.get_at(1) == 5
    assert a.get_at(2) == 10
    assert a.get_at(3) == None
    
    # Test length and is_empty
    assert a.length() == 3
    assert a.is_empty() == False
    
    # Test insert_at
    a.insert_at(1, 20)
    assert a.toList() == [15, 20, 5, 10]
    
    a.insert_at(0, 25)
    assert a.toList() == [25, 15, 20, 5, 10]
    
    a.insert_at(5, 30)
    assert a.toList() == [25, 15, 20, 5, 10, 30]
    
    # Test delete_at
    assert a.delete_at(1) == 15
    assert a.toList() == [25, 20, 5, 10, 30]
    
    assert a.delete_at(0) == 25
    assert a.toList() == [20, 5, 10, 30]
    
    assert a.delete_at(3) == 30
    assert a.toList() == [20, 5, 10]
    
    # Test resize functionality
    b = Aseq()
    for i in range(10):
        b.insert_last(i)
    assert b.length() == 10
    assert b.capacity >= 10
    
    # Test empty sequence
    c = Aseq()
    assert c.is_empty() == True
    assert c.length() == 0
    assert c.toList() == []
    
    print("All tests passed!")

if __name__ == "__main__":
    test_aseq()