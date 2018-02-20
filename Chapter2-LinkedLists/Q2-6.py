from linkedlist import Node

def check_palindrome(head):
    if head is None:
        return False

    reversed_linked_list = Node(head.data)
    reversed_linked_list.next = None
    current_node = head.next

    #reverse the list
    while current_node is not None:
        new_node = Node(current_node.data)
        new_node .next = reversed_linked_list
        reversed_linked_list = new_node
        current_node = current_node.next

    current_node = head

    while current_node is not None and reversed_linked_list is not None:
        if current_node.data != reversed_linked_list.data:
            return False
        current_node = current_node.next
        reversed_linked_list = reversed_linked_list.next

    return True

print("============== TEST 1 ==================")
test_list1 = Node('a')
test_list1.createLinkedListFromList(['b', 'a'])
result1 = check_palindrome(test_list1)

print(result1)

print("============== TEST 2 ==================")
test_list2 = Node('a')
test_list2.createLinkedListFromList(['b', 'b'])
result2 = check_palindrome(test_list2)

print(result2)
