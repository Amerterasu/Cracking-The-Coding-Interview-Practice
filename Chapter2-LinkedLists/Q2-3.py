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

#much better version
#remember that deleting a node is just rearranging its next pointer to skip the one we want to delete
#also I don't have to shift the whole linked list
#finally and most importantly, look at the linked list as a whole. Realize that what we were trying to achieve didn't require shifting the whole array
# ex. 1->2->3->4->5 and we want to delete 3 then we would get 1->2->4->5
# from this example we should realize that the 4 is in the old place of the three!
def better_del_middle_node(mNode):
    if mNode is None or mNode.data == None:
        return False

    mNode.data = mNode.next.data
    mNode.next = mNode.next.next
    return True

testLinkedlist = Node(1)
testLinkedlist.createLinkedListFromList([2,3,4,5])
targetNode = getNode(testLinkedlist, 3)

better_del_middle_node(targetNode)

testLinkedlist.printLinkedList()

testLinkedlist2 = Node(1)
testLinkedlist2.createLinkedListFromList([2,3,9,5])
targetNode2 = getNode(testLinkedlist2, 9)

better_del_middle_node(targetNode2)

testLinkedlist2.printLinkedList()
