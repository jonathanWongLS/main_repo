from typing import List

class PriorityQueue():
    def __init__(self):
        self.queue = list()
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def add(self, priority, item):
        self.queue.append((priority, item))
        self.length += 1

    def pop(self):
        min_item = None
        new_list = []
        if self.length == 0:
            raise EmptyQueue()
        else:
            min = self.queue[0][0]
            for i in range(len(self.queue)):
                if self.queue[i][0] <= min:
                    min = self.queue[i][0]
            
            for i in range(len(self.queue)):
                if self.queue[i][0] == min:
                    min_item = self.queue[i]
                    self.queue[i] = None
            
            for i in range(len(self.queue)):
                if self.queue[i] is not None:
                    new_list.append(self.queue[i])
                
            self.queue = new_list

        self.length -= 1

        return min_item[1]

    def peek(self):
        if len(self.queue) == 0:
            raise EmptyQueue()
        else:
            min = self.queue[0][0]
            for i in range(len(self.queue)):
                if self.queue[i][0] <= min:
                    min = self.queue[i][0]
            
            for i in range(len(self.queue)):
                if self.queue[i][0] == min:
                    min_item = self.queue[i]

        return min_item[1]

    def __str__(self):
        return str(self.queue)
            
class EmptyQueue(Exception):
    def __init__(self, message = "Queue is empty!"):
        print(message)


if __name__ == '__main__':
    prio = PriorityQueue()
    print(prio.isEmpty())
    
    
