class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def appendToEnd(self, data):
        currentNode = self
        newNode = Node(data)
        while currentNode.next is not None:
            currentNode = currentNode.next
        
        currentNode.next = newNode
        
    def createLinkedListFromList(self, l):
        currentNode = self
        for num in l:
            newNode = Node(num)
            currentNode.next = newNode
            currentNode = currentNode.next
            
    def printLinkedList(self):
        currentNode = self
        l = []
        while currentNode is not None:
            l.append(currentNode.data)
            currentNode = currentNode.next
        print(l)
        
        