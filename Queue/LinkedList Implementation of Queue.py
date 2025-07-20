class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

class Queue:
    def __init__(self):
        self.front= self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        new_node= Node(data)
        if self.is_empty():
            self.front= self.rear= new_node
        else:
            self.rear.next= new_node
            self.rear= new_node
        self.printQueue()

    def dequeue(self):
        if self.is_empty():
            return 
        temp= self.front
        self.front= self.front.next
        if self.front is None:
            self.rear= None
        self.printQueue()

    def printQueue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp= self.front
        queue_string= "Current Queue: "
        while temp is not None:
            queue_string+= str(temp.data) + " "
            temp = temp.next
        print(queue_string)
q= Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.printQueue()


        





