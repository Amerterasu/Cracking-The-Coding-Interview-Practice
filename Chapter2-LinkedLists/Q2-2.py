from linkedlist import Node
def findKToLast(head, K):
    lastKElm = {}

    currentNode = head
    counter = 1
    kNode = head
    while counter <= K:
        if counter == K:
            kNode = currentNode
        elif counter < K:
            currentNode = currentNode.next
        if currentNode.next is None:
            return kNode

        kNode = kNode.next
