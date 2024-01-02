class MinHeap:
    def __init__(self, data):
        self.arr = []
        self.peek = None
        if data:
            self.arr.append(data.pop(0))
            for item in data:
                self.add(item)
            self.peek = self.arr[0]
    def __str__(self):
        return f"MinHeap({self.arr})"
    def add(self, item):
        i = len(self.arr)
        self.arr.append(item)
        while True:
            if i % 2 == 1:
                p_i = int((i-1)/2)
            else:
                p_i = int((i-1)/2)
            if self.arr[i] < self.arr[p_i]:
                self.arr[i], self.arr[p_i] = self.arr[p_i], self.arr[i]
                i = p_i
            else: break
        self.peek = self.arr[0]
        return self
    def removePeek(self):
        i = 0
        if len(self.arr) < 1:
            raise Exception("Heap is empty")
        if len(self.arr) == 1:
            self.arr = []
            self.peek = None
            return self
        self.arr[i] = self.arr.pop()
        if (len(self.arr) == 2):
            if self.arr[0] > self.arr[1]:
                self.arr[0], self.arr[1] = self.arr[1], self.arr[0]
        while (2*i+2) < len(self.arr) and (self.arr[i] > self.arr[2*i+1] or self.arr[i] > self.arr[2*i+2]):
            if self.arr[2*i+1] < self.arr[2*i+2]:
                self.arr[i], self.arr[2*i+1] = self.arr[2*i+1], self.arr[i]
                i = 2*i+1
            else:
                self.arr[i], self.arr[2*i+2] = self.arr[2*i+2], self.arr[i]
                i = 2*i+2
        self.peek = self.arr[0]
        return self
    def popPeek(self):
        value = self.peek
        self.removePeek()
        return value

heap = MinHeap([10, 15])
print(heap)
print(heap.add(25))
print(heap.add(100))
print(heap.removePeek())
print(heap.popPeek())
print(heap)
