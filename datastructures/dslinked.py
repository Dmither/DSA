class DSLinked:
    def __init__(self, *args):
        self.value = args[0]
        if (len(args) > 1):
            self.next = DSLinked(*args[1:])
        else: self.next = None
    def __str__(self):
        result = str(self.value)
        if (self.next != None):
            result += ", " + str(self.next) 
        return result
    def reversestr(self):
        result = str(self.value)
        if (self.next != None):
            result = self.next.reversestr() + ", " + result 
        return result
    def size(self):
        if (self.next == None): return 1
        return 1 + self.next.size()
    def getLast(self):
        if self.next:
            return self.next.getLast()
        return self