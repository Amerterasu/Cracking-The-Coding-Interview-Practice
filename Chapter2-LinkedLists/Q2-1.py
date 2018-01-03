from linkedlist import Node

def removeDup(head):
    foundData = set()
    foundData.add(head.data)
    
    currentNode = head
    while currentNode.next is not None:
        if currentNode.next.data in foundData:
            currentNode.next = currentNode.next.next
        else:
            currentNode = currentNode.next
            foundData.add(currentNode.data)

def removeDup2(head):

    currentNode = head
    searchNode = head

    #extra while loop condition because it's possible that in the process of deletion we changed the next node to be none and
    # it naively changes it to none
    while currentNode is not None and currentNode.next is not None:
        searchNode = currentNode
        while searchNode.next is not None:
            if searchNode.next.data == currentNode.data:
                searchNode.next = searchNode.next.next
            else:
                searchNode = searchNode.next
        currentNode = currentNode.next

print("===========Test 1==========")
head = Node(4)
head.createLinkedListFromList([5,6,4])
head.printLinkedList()
removeDup(head)
print("Remove Duplicates")
head.printLinkedList()

print("===========Test 2==========")
head2 = Node(1)
head2.createLinkedListFromList([1,1,1,1,2,2,3,3])
head2.printLinkedList()
print("Remove Duplicates")
removeDup(head2)
head2.printLinkedList()

print("===========Test 3==========")
head3 = Node(4)
head3.createLinkedListFromList([5,6,4])
head3.printLinkedList()
print("Remove Duplicates")
removeDup2(head3)
head3.printLinkedList()

print("===========Test 4==========")
head4 = Node(1)
head4.createLinkedListFromList([1,1,3,4,1,2,2,2,3,3])
head4.printLinkedList()
print("Remove Duplicates")
removeDup2(head4)
head4.printLinkedList()