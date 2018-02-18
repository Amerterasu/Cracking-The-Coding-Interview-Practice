def del_middle_node(mNode):
    currentNode = mNode

    while currentNode.next.next is not None:
        currentNode.data = currentNode.next.data
        currentNode = currentNode.next

    currentNode.data = currentNode.next.data
    currentNode.next = None
