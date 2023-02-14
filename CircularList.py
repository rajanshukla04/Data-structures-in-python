class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLinkedList:
    def createList(self):
        self.root=None
        self.last=None

    def insertLeft(self,data):
        n=Node(data)
        if self.root==None:#no root there
            self.root=self.last=n
            self.last.next=self.root
        else:
            n.next=self.root#1
            self.root=n#2
            self.last.next=self.root#3
        print("Added to List")
    
    def deleteLeft(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            if self.root==self.last:#only one node
                self.root=self.last=None
            else:
                self.root=self.root.next
                self.last.next=self.root
            
            print(t.data,"Deleted")

    def insertRight(self,data):
        n=Node(data)
        if self.root==None:#no root there
            self.root=self.last=n
            self.last.next=self.root
        else:
            self.last.next=n
            self.last=n
            self.last.next=self.root
        print("Added to List")

    def deleteRight(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            if self.root==self.last:#only one node
                self.root=self.last=None
            else:
                t=t2=self.root#1
                while t!=self.last:#2
                    t2=t
                    t=t.next
                self.last=t2#3
                self.last.next=self.root#4
            print(t.data,"Deleted")
            
    def printList(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            while True:
                print("[",t.data,"]->",end="")
                t=t.next
                if t==self.root:
                    break
obj=CircularLinkedList()
obj.createList()
while True:
    print("\n1.Insert Left\n2.Delete Left\n3.Insert Right\n4.Delete Right\n5.Print\n0.Exit:")
    ch=int(input("Enter:"))
    if ch==1:
        data=int(input("Enter data:"))
        obj.insertLeft(data)
    
    elif ch==2:
        obj.deleteLeft()
    
    elif ch==3:
        data=int(input("Enter data:"))
        obj.insertRight(data)
    
    elif ch==4:
        obj.deleteRight()
    
    elif ch==5:
        obj.printList()  
        
    elif ch==0:
        print("devloped by amarpanchal.education")
        break
    else:
        print("Wrong input")
