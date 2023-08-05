from dslinked import DSLinked

class DSStack:
    """
    Стек, заснований на зв'язному списку.
    Поля:
        peek - верхній елемент стеку
        size - повертає кількість елементів
        is_empty - перевіряє, чи не порожній
    Методи:
        clear() - очищає стек
        push(val) - додає нове значення зверху стеку
        pop() - знімає та повертає значення зверху стеку
    """
    def __init__(self, *args):
        if len(args):
            self.head = DSLinked(*args[::-1])
            self.peek = self.head.value
            self.size = self.head.size()
            self.is_empty = False
        else: self.clear()
    def __str__(self):
        if (self.head):
            return "Stack(" + self.head.reversestr() + ")"
        return "Stack()"
    def clear(self): 
        self.head = None
        self.peek = None
        self.size = 0
        self.is_empty = True
    def push(self, value):
        next = self.head
        self.head = DSLinked(value)
        self.head.next = next
        self.peek = self.head.value
        self.size += 1
        return self
    def pop(self):
        if not self.head: return self
        if not self.head.next: self.clear()
        else:
            self.head = self.head.next
            self.peek = self.head.value
            self.size -= 1
        return self

ls = DSStack(1, 2, 3)
print(ls)
print(ls.peek, ls.size, ls.is_empty, sep=" | ")
ls.pop()
print(ls.peek, ls.size, ls.is_empty, sep=" | ")
ls.pop()
print(ls.peek, ls.size, ls.is_empty, sep=" | ")
ls.pop()
print(ls.peek, ls.size, ls.is_empty, sep=" | ")
ls.pop()
print(ls.peek, ls.size, ls.is_empty, sep=" | ")
ls.pop()
print(ls.peek, ls.size, ls.is_empty, sep=" | ")
ls.push("a")
print(ls.peek, ls.size, ls.is_empty, sep=" | ")
ls.push("a")
print(ls.peek, ls.size, ls.is_empty, sep=" | ")
ls.push("a")
print(ls.peek, ls.size, ls.is_empty, sep=" | ")