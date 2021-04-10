class Node:
    def __init__(self,data = None):
        self.data = data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlst(self):
        temp = self.head
        
        while temp:
            print(temp.data)
            temp = temp.Next
    def addbigging(self,newdata):
        nd = Node(newdata)
        nd.Next = self.head
        self.head = nd

lst = LinkedList()
lst.head = Node(7)
e = Node(4)
e2 = Node(5)
e4 = Node(6)
lst.head.Next = e
e.Next = e2
e2.Next = e4
lst.addbigging(99)
lst.addbigging(33)
lst.printlst()
