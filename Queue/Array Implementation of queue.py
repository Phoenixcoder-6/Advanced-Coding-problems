class Queue:
    def __init__(self):
        self.q= []

    def is_empty(self):
        return len(self.q) == 0
    
    def enqueue(self,x):
        self.q.append(x)

    def dequeue(self):
        if not self.is_empty():
            self.q.pop(0)
    
    def get_front(self):
        if self.is_empty():
            return -1
        else:
            self.q[0]

    def display(self):
        print(''.join(map(str,self.q)))


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    q.dequeue()
    q.display()