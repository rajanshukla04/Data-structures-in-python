#Stack Emplimention 

class DS1:
    stack=[]
    tos=0
    MaxSize=0
    def createStack(self,size):
        DS1.tos=-1
        DS1.MaxSize=size
        for i in range(size):
            DS1.stack.append(0)
        print("stack created of size",len(DS1.stack))
        print(DS1.stack)
    def push(self,e):
        DS1.tos+=1
        DS1.stack[DS1.tos]=e
        print("Element pushed")
        
    def pop(self):
        temp=DS1.stack[DS1.tos]
        DS1.tos-=1
        return(temp)
    def isFull(self):
        if DS1.tos==DS1.MaxSize-1:
            return True
        else:
            return False
    def isEmpty(self):
        if DS1.tos==-1:
            return True
        else:
            return False
    def peek(self):
        return(DS1.stack[DS1.tos])
    def printStack(self):
        for i in range(DS1.tos,-1,-1):
            print(i)
            print(DS1.stack[i])

#Main Code
o=DS1()
o.createStack(int(input("Enter size:")))
while True:
    print("1.Push\n2.Pop\n3.Peek\n4.Print\n0.Exit")
    ch=int(input("Enter:"))
    if ch==1:
        if o.isFull()!=True:
            data=int(input("Enter data:"))
            o.push(data)
            print("Element pushed")
        else:
            print("Stack Full")
    elif ch==2:
        if o.isEmpty()!=True:
            print("Element poped:",o.pop())
        else:
            print("Stack Empty")
    elif ch==3:
        if o.isEmpty()!=True:
            print("Element @peek:",o.peek())
        else:
            print("Stack Empty")
    elif ch==4:
        if o.isEmpty()!=True:
            print("Elements is stack")
            o.printStack()
        else:
            print("Stack Empty")
        
    elif ch==0:
        print("devloped by Rajan Shukla")
        break
    else:
        print("Wrong input")
         
    """
Stack:
----Linear
----Mostly Static 
----One sided 
----LIFO  Property 
"""
#ADT
'''
1. create Stack 
--tos<--- -1
-maxsizse <--1

---|
   |
   |


2. Push(e)
insert data on Stack 
tos+1

3. isFull(): True if stack is full 
    .if  tos ==maxsize-1 full or not 

4. POP(). 
  REMOVe element in LIFO manner 
  tos =tos -1 

5. isEmpty():
  if tos==-1  then true 
  or else false 

6. atPeek():
  return the elemnet at top 

7. print stack :
    print in LIFO manner 
'''
         
         
