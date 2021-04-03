class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def printlst(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def addbig(self,newdata):
        nd = Node(newdata)
        nd.next = self.head
        self.head = nd


n = List()
n.head = Node("rushi")
n1 = Node("shri")
n.head.next = n1
n.addbig('rs')
n.printlst()