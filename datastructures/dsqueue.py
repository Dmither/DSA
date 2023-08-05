from dslinked import DSLinked

class DSQueue:
    """
    Черга, заснована на зв'язному списку.
    Поля:
        first - перший доданий,
        last - останній доданий
        size - повертає кількість елементів
        is_empty - перевіряє, чи не порожній
    Методи:
        clear() - очищає чергу
        enqueue(val) - додає нове значення в кінець черги
        dequeue() - знімає та повертає значення з початку черги
    """
    def __init__(self, *args):
        if len(args):
            self.head = DSLinked(*args[::-1])
            self.last = self.head.getLast()
            self.first = self.head.value
            self.size = self.head.size()
            self.is_empty = False
        else: self.clear()

    def __str__(self):
        if (self.head):
            return "Queue(" + self.head.reversestr() + ")"
        return "Queue()"
    def clear(self):
        self.head = None
        self.last = None
        self.first = None
        self.size = 0
        self.is_empty = True
    def enqueue(self, value):
        if self.last:
            addition = DSLinked(value)
            DSLinked.next = None
            self.last.next = addition
            self.last = addition
            self.size += 1
        else:
            self.head = DSLinked(value)
            self.last = self.head.getLast()
            self.first = self.head.value
            self.size = self.head.size()
            self.is_empty = False
        return self
    def dequeue(self):
        if not self.head:
            return self
        if self.head.next:
            self.head = self.head.next
            self.first = self.head.value
            self.size -= 1
        else: self.clear()
        return self


lq = DSQueue(1, 2, 3, 4)
print(lq)
print(lq.last, lq.first, lq.size, lq.is_empty, sep=" | ")
lq.enqueue("a")
print(lq.last, lq.first, lq.size, lq.is_empty, sep=" | ")
lq.dequeue()
print(lq.last, lq.first, lq.size, lq.is_empty, sep=" | ")
lq.dequeue()
print(lq.last, lq.first, lq.size, lq.is_empty, sep=" | ")
lq.dequeue()
lq.dequeue()
lq.dequeue()
lq.dequeue()
lq.dequeue()
print(lq.last, lq.first, lq.size, lq.is_empty, sep=" | ")
lq.enqueue("a")
print(lq.last, lq.first, lq.size, lq.is_empty, sep=" | ")
lq.enqueue("b")
print(lq.last, lq.first, lq.size, lq.is_empty, sep=" | ")
lq.dequeue()
lq.dequeue()
lq.dequeue()
lq.dequeue()
lq.dequeue()
print(lq.last, lq.first, lq.size, lq.is_empty, sep=" | ")