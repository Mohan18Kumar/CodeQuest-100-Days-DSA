class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def  insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)

input_str = input("Enter the elements: ")
values = list(map(int,input_str.strip().split()))
root = None
for val in values:
    root = insert(root,val)

inorder(root)
print()