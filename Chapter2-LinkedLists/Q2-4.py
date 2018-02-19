from linkedlist import Node

def assign_to_partition(left_partition, right_partition, partition, node):
    if node.data < partition:
        if left_partition is None:
            left_partition = node
        else:
            left_partition.next = node
            left_partition = left_partition.next
    else:
        if right_partition is None:
            right_partition = node
        else:
            right_partition.next = node
            right_partition = right_partition.next
    return (left_partition, right_partition)

def partition_linked_list(head, partition):
    left_partition = None
    right_partition = None
    left_head = None
    right_head = None
    current_node = head

    # left_partition, right_partition = assign_to_partition(left_partition, right_partition, partition, current_node)
    # if left_partition is not None:
    #     newHead = left_partition
    # else:
    #     newHead = right_partition
    #
    # current_node = current_node.next

    while current_node is not None:
        left_partition, right_partition = assign_to_partition(left_partition, right_partition, partition, current_node)
        if left_head is None and left_partition is not None:
            left_head = left_partition
        if right_head is None and right_partition is not None:
            right_head = right_partition
        current_node = current_node.next

    #merge the two partition halves
    #We want to attach it to the head of the right partition!
    left_partition.next = right_head

    if right_partition is not None:
        right_partition.next = None

    return left_head

testLinkedList = Node(1)
testLinkedList.createLinkedListFromList([2,7,3,9])
result_linked_list = partition_linked_list(testLinkedList, 5)
result_linked_list.printLinkedList()

#book test
testLinkedList2 = Node(3)
testLinkedList2.createLinkedListFromList([5,8,5,10,2,1])
result_linked_list2 = partition_linked_list(testLinkedList2, 5)
result_linked_list2.printLinkedList()
