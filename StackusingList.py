class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class DynamicStack:
    def createStack(self):
        self.tos=None
    
    def push(self,data):
        n=Node(data)
        if self.tos==None:#no root there
            self.tos=n
        else:
            n.next=self.tos#1
            self.tos=n#2
        print("Element Pushed:")
    
    def pop(self):
        if self.tos==None:
            print("Empty Stack")
        else:
            t=self.tos
            self.tos=self.tos.next
            print(t.data,"Poped")

    def printStack(self):
        if self.tos==None:
            print("Empty Stack")
        else:
            t=self.tos
            while t!=None:
                print(t.data)
                t=t.next

obj=DynamicStack()
obj.createStack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.printStack()
obj.pop()
obj.pop()
obj.printStack()