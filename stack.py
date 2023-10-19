'''Стек на односвязном списке'''
class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value

class Stack:
    def __init__(self):
        self._top = None
        self._count = 0
    
    def append(self, value):
        new_node = Node(value)
        if self._top != None:
            new_node.next = self._top
        self._top = new_node
        self._count += 1
    
    def pop(self):
        if self._count == 0:
            raise ValueError('Stack is empty')
        value = self._top.value
        self._top = self._top.next
        self._count -= 1
        return value
        
    def peek(self):
        if self._count == 0:
            raise ValueError('Stack is empty')
        value = self._top.value
        return value
        
    def insert(self, value, depth):
        if depth == 0:
            self.append(value)
            return
        depth -= 1
        node = self._top
        while depth != 0 and node != None:
            node = node.next
            depth -= 1     
        new_node = Node(value, node.next)
        node.next = new_node
        self._count += 1
    
    '''Метод 'вращает' первые depth элементов turns раз'''
    def roll(self, turns, depth):
        turns = turns % depth
        start = self._top
        current = self._top
        if turns == 0:
            return
        for _ in range(turns - 1):
            current = current.next
        end = current
        for _ in range(depth - turns):
            current = current.next
        border = current
        self._top = end.next
        end.next = border.next
        border.next = start
    
    'Возвращает первые count элементов стека начиная с верхнего'
    def values(self, count):
        current = self._top
        while count > 0 and current != None:
            yield current.value
            count -= 1
            current = current.next

    def count(self):
        return self._count