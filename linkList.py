class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def createList(self):
        self.root=None
    
    def insertLeft(self,data):
        n=Node(data)
        if self.root==None:#no root there
            self.root=n
        else:
            n.next=self.root#1
            self.root=n#2
        print("Added to List")
    
    def deleteLeft(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            self.root=self.root.next
            print(t.data,"Deleted")

    def insertRight(self,data):
        n=Node(data)
        if self.root==None:#no root there
            self.root=n
        else:
            t=self.root#1
            while t.next!=None:#2
                t=t.next
            t.next=n#3
        print("Added to List")

    def deleteRight(self):
        if self.root==None:
            print("Empty List")
        else:
            t=t2=self.root#1
            while t.next!=None:#2
                t2=t
                t=t.next
            t2.next=None#3
            print(t.data,"Deleted")#
            
    def printList(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            while t!=None:
                print("[",t.data,"]->",end="")
                t=t.next

    def searchList(self,key):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            while t!=None and t.data!=key:
                t=t.next
            if t==None:
                print("Not Found")
            else:
                print("Found")

obj=LinkedList()
obj.createList()
while True:
    print("\n1.Insert Left\n2.Delete Left\n3.Insert Right\n4.Delete Right\n5.Print\n6.Search\n0.Exit:")
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
    
    elif ch==6:
        key=int(input("Enter data to search:"))
        obj.searchList(key)
        
    elif ch==0:
        print("devloped by Rajan Shukla ")
        break
    else:
        print("Wrong input")