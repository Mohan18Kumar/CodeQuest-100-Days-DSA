class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for va1 in values[1:]:
        current.next = Node(va1)
        current = current.next
    return head
def print_linked_list(head):
    current = head
    element = []
    while current:
        element.append(str(current.data))
        current = current.next
    print("Linked List:"," -> ".join(element))
values = list(map(int, input("Enter values for the linked list:").strip().split()))
head = build_linked_list(values)
print_linked_list(head)                    
        