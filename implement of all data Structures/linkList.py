class  Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def createList(self):
        self.root=None
    def insertLeft(self,data):
        n=Node(data)
        if self.root==None:   #no Node is there 
            self.root=n
        else:
            n.next=self.root
            self.root=n
        print("Added to list")

    def deleteLeft(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            self.root=self.root.next   #set head node 
            print(t.data,"Delelet")

    def insertRight(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            t=self.root  #it form root 1 
            while t.next!=None:
                t=t.next
            t.next=n
        print("Added to List")
    def deleteRight(self):
        if self.root==None:
            print("Empty list ")
        else:
            t=t2=self.root
            while t!=None:
                t2=t
                t=t.next
            t2.next=None
            print(t.data,"DEeleted ")
    def reversList(self):
        prev=Node(None)
        current=self.root
        next=Node(None)
        while(current.next!=None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.root=prev


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
            print('Empty LIst ')
        else:
            t=t.root
            while t!=None and t.data==key:
                t=t.next
            if t==None:
                print("NOt Fount ") 
            else:
                print("found ")
    
obj=LinkedList()
obj.createList()

while True:
    print("\n1.InsertLeft\n2.Deleted Left \n3.insertRight \n4.Deleteright \n5.print \n6 ReversList \n7 Search in List \n0 exit\n")
    ch=int(input("Enter you choice"))
    if ch==1:
        data=int(input("Enter data "))
        obj.insertLeft(data)
    elif ch==2:
        obj.deleteLeft()
        
    elif ch==3:
        data=int(input("Enter data "))
        obj.insertRight(data)
    elif ch==4:
        obj.deleteRight()
    elif ch==5:
        obj.printList()
    elif ch==6:
        obj.reversList()
    elif ch==7:
        key=int(input("Enter data to search:"))
        obj.searchList(key)
    elif ch==0:
        print("devloped by Rajan Shukla")
        break
    else:
        print("Wrong input")
