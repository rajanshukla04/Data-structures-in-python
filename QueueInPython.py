class DS:
    q=[]
    front=0
    rear=0
    MaxSize=0
    def createQueue(self,size):
        DS.MaxSize=size
        DS.front=0
        DS.rear=-1
        for i in range(DS.MaxSize):
            DS.q.append(0)
    def Enqueue(self,e):
        DS.rear+=1
        DS.q[DS.rear]=e
    def isFull(self):
        if DS.rear==DS.MaxSize-1:
            return True
        else:
            return False

    def Dequeue(self):
        t=DS.q[DS.front]
        DS.front+=1
        return t

    def isEmpty(self):
        if DS.front>DS.rear:
            return True
        else:
            return False

    def printQueue(self):
        for i in range(DS.front,DS.rear+1):
            print(DS.q[i])

#Main Code
o=DS()
o.createQueue(int(input("Enter size:")))
while True:
    print("1.Enqueue\n2.Dequeue\n3.Print\n0.Exit")
    ch=int(input("Enter:"))
    if ch==1:
        if o.isFull()!=True:
            data=int(input("Enter data:"))
            o.Enqueue(data)
            print("Element pushed")
        else:
            print("Queue Full")
    elif ch==2:
        if o.isEmpty()!=True:
            print("Element dequeued:",o.Dequeue())
        else:
            print("Queue Empty")
    elif ch==3:
        if o.isEmpty()!=True:
            print("Elements is squeue")
            o.printQueue()
        else:
            print("Queue Empty")
        
    elif ch==0:
        print("devloped by amarpanchal.education")
        break
    else:
        print("Wrong input")
