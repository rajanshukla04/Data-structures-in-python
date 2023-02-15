class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class DoubleLinkedList():
    def createList(self):
        self.root=None
        self.last=None
    def insertLeft(self,data):
        n=Node(data)
        if self.root==None:
            self.root=self.last=n
            self.last.next=self.root
        else:
            n.next=self.root
            self.root=n
            self.last.next=self.root
        print('Added the item in the list ')
# Deleted the object form the lef
    def DeletedLeft(self):
        if self.root==None:
            print("Empty linked list ")
        else:
            t=self.root
            if self.root==self.last:
                self.root=self.last=None
            else:
                self.root=self.root.next
                self.last.next=self.root
        print(t.data,"Deleted ")


# add the iteam into the rightplace 
    def insertRight(self,data):
        n=Node(data)
        if self.root==None:
            self.root=self.last=n
            self.last.next=self.root
        else:
            self.last.next=n
            self.last=n
            self.last.next=self.root
        print("The iteam is added ")
 # Deleted the object from the right 

    def deletedRight(self):
        if self.root==None:
            print("Empty List ")
        else:
            t=self.last
            if self.root==self.last:
                self.root=self.last=None
            else:
                t=t2=self.root
                while t!=self.last:
                    t2=t
                    t=t.next
                self.last=t2
                self.last.next=self.root
            print(t.data,"Deleted ")
# print the list
    def printList(self):
        if self.root==None:
            print("Empty list ")
        else:
            t=self.root
            while True:
                print("[",t.data,"]->",end=" ")
                t=t.next
                if t==self.root:
                    break
        print()
    def searchList(self,key):
        if self.root==None:
            print("Empty list ")
        else:
            t=self.root
            while t.data!=key:
                t=t.next
                if t==self.last.next:
                    t=None
                    break
            if t==None:
                print("not found ")
            else:
                print(t.data,"found ")
    
        
obj=DoubleLinkedList()
obj.createList()
while True:
    print("1.insert left \n2.Deleted form left \n3. Insert Right  \n4. Deleted Right  \n5.print object\n6. Search  object in list \n7.break")
    ch=int(input("Enter you choice "))
    if ch==1:
        data=int(input("Enter your data "))
        obj.insertLeft(data)
    elif ch==2:
        obj.DeletedLeft()
    elif ch==3:
        data=int(input("Enter your Right object  "))
        obj.insertRight(data)
    elif ch==4:
        obj.deletedRight()
    elif ch==5:
        obj.printList()
    elif ch==6:
        key=int(input("Enter the object for search "))
        obj.searchList(key)
    elif ch==7:
        print("Developed by Rajan Shukla ")
        break
    else:
        print("Worng input ")
        