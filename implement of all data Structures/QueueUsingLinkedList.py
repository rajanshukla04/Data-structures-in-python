class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class DyanmicQueue:
    
    def createQueue(self):
        self.front=None
        self.rear=None
    
    def dequeue(self):
        if self.front==None:
            print("Empty Queue")
        else:
            t=self.front
            self.front=self.front.next
            print(t.data,"Dequeued")

    def enqueue(self,data):
        n=Node(data)
        if self.front==None:#no root there
            self.front=self.rear=n
        else:
            self.rear.next=n
            self.rear=n
        print("Added to Queue")

              
    def printQueue(self):
        if self.front==None:
            print("Empty Queue")
        else:
            t=self.front
            while t!=None:
                print("[",t.data,"]-",end="")
                t=t.next

obj=DyanmicQueue()
obj.createQueue()
obj.enqueue(100)
obj.enqueue(200)
obj.enqueue(300)
obj.enqueue(400)
obj.printQueue()
obj.dequeue()
obj.printQueue()