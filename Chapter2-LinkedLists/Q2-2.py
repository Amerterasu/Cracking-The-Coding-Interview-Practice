from linkedlist import Node
def findKToLast(head, K):
    lastKElm = {}

    currentNode = head
    counter = 1
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
        

