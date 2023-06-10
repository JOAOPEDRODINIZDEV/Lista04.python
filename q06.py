class Item:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size += 1
        
    def is_empty(self):
        return self.head is None
    
    def enqueue(self,value):
        new_item = Item(value)
        if self.is_empty():
            self.tail = new_item
            self.head = new_item
        else:
            self.tail.next = self.tail
            self.tail = new_item
        self.size += 1
        
    def dequeue(self):
        if self.is_empty:
            raise IndexError("")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return value
    
    def get_size(self):
        return self.size 