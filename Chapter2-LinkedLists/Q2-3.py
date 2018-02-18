from linkedlist import Node

def del_middle_node(mNode):
    currentNode = mNode

    while currentNode.next.next is not None:
        currentNode.data = currentNode.next.data
        currentNode = currentNode.next

    currentNode.data = currentNode.next.data
    currentNode.next = None

def getNode(head, targetNode):
    currentNode = head
    while currentNode is not None:
        if currentNode.data == targetNode:
            return currentNode
        currentNode = currentNode.next

    return None

testLinkedlist = Node(1)
testLinkedlist.createLinkedListFromList([2,3,4,5])
targetNode = getNode(testLinkedlist, 3)

del_middle_node(targetNode)

testLinkedlist.printLinkedList()

testLinkedlist2 = Node(1)
testLinkedlist2.createLinkedListFromList([2,3,9,5])
targetNode2 = getNode(testLinkedlist2, 9)

del_middle_node(targetNode2)

testLinkedlist2.printLinkedList()
