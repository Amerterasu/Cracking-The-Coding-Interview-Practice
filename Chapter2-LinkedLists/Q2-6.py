from linkedlist import Node

def check_palindrome(head):
    if head is None:
        return False
    current_node = head
    node_data = [head.data]
    preivious_node = head
    head.next = None
    current_node = current_node.next
    index = 0

    while current_node is not None:
        node_data.append(current_node.data)
        two_ago_node = preivious_node
        one_ago_node = current_node
        current_node = current_node.next
        one_ago_node.next = two_ago_node
        preivious_node = one_ago_node




    #after reversing the list, we check if it's the same as it is forward
    current_node = preivious_node
    while current_node is not None:
        if index >= len(node_data) or current_node.data != node_data[index]:
            return False
        index += 1
        current_node = current_node.next

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
