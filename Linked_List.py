class Elem:
    def __init__ (self, value = None):
        self.value = value
        self.nextElem = None

class LinkedList:
    def __init__(self , *elems):
        self.head = None
        for elem in elems[0]:
            self.push(elem)

    def __repr__(self):
        current = self.head
        str = '[ '
        while current is not None:
            str += f'{current.value},'
            current = current.nextElem
        str += ']'
        return str

    def contains(self, value):
        lastElem = self.head
        while (lastElem):
            if value == lastElem.value:
                return True
            else:
                lastElem = lastElem.nextElem
        return False

    def push(self, value):
        newElem = Elem(value)
        if self.head is None:
            self.head = newElem
            return
        lastElem = self.head
        while (lastElem.nextElem):
            lastElem = lastElem.nextElem
        lastElem.nextElem = newElem

    def get(self, index):
        lastElem = self.head
        elemIndex = 0
        while elemIndex <= index:
            if elemIndex == index:
                return lastElem.value
            elemIndex = elemIndex + 1
            lastElem = lastElem.nextElem

    def remove(self, value):
        current = self.head
        if current is not None:
            if current.value == value:
                self.head = current.nextElem
                return
        while current is not None:
            if current.value == value:
                break
            last = current
            current = current.nextElem
        if current == None:
            return
        last.nextElem = current.nextElem

    def printList(self):
        current = self.head
        while current is not None:
            print(current.value, end=' ')
            current = current.nextElem