from linkedlist import Node
def findKToLast(head, K):
    currentNode = head
    counter = 0
    kNode = head
    while currentNode is not None:
        if counter < K:
            counter += 1
        else:
            kNode = kNode.next
        currentNode = currentNode.next
        
    if counter == K:
        return kNode
    else:
        return None

testLinkedList = Node(1)
testLinkedList.createLinkedListFromList([2,3,4])
result = findKToLast(testLinkedList, 4)
print(result.data)

        

