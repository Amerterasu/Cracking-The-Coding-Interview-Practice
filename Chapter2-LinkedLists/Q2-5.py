from linkedlist import Node

def add_nodes(n1, n2):
    result = 0
    if n1 is None:
        result = n2.data
    elif n2 is None:
        result = n1.data
    else:
        result = n1.data + n2.data

    return result

def add_linked_list(n1, n2):
    p1 = n1
    p2 = n2
    head = None
    new_linked_list = head
    carry = 0

    if p1.data == 0 and p2.data != 0:
        return p2
    elif p2.data == 0 and p1.data != 0:
        return p1

    while p1 is not None or p2 is not None:
        result = add_nodes(p1, p2)
        result += carry

        if result >= 10:
            carry = 1
        else:
            carry = 0

        new_data = result % 10
        new_node = Node(new_data)
        if head is None:
            head = new_node
            new_linked_list = new_node
        else:
            new_linked_list.next = new_node
            new_linked_list = new_node
        if p1 is not None:
            p1 = p1.next
        if p2 is not None:
            p2 = p2.next

    if carry == 1:
        new_linked_list.next = Node(1)

    return head

print("============= TEST 1 ===============")
num1 = Node(1)
num2 = Node(2)
result1 = add_linked_list(num1, num2)
result1.printLinkedList()

print("============= TEST 2 ===============")
num3 = Node(5)
num3.createLinkedListFromList([6,7])
num4 = Node(4)
num4.createLinkedListFromList([8,9])
result2 = add_linked_list(num3, num4)
result2.printLinkedList()

print("============= TEST 3 ===============")
num5 = Node(5)
num5.createLinkedListFromList([6,7])
num6 = Node(4)
result3 = add_linked_list(num5, num6)
result3.printLinkedList()

print("============= TEST 4 ===============")
num7 = Node(0)
num7.createLinkedListFromList([0,1])
num8 = Node(0)
num8.next = Node(5)
result4 = add_linked_list(num7, num8)
result4.printLinkedList()

print("============= TEST 5 ===============")
num9 = Node(0)
num10 = Node(9)
result5 = add_linked_list(num9, num10)
result5.printLinkedList()
