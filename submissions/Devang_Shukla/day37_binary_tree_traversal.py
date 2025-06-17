class Node:
    def _init_(self, value):
        self.data = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)
def main():
    nums = list(map(int, input("Enter integers to build binary tree: ").split()))
    root = None
    for num in nums:
        root = insert(root, num)

    print("In-Order Traversal:")
    inorder_traversal(root)

if __name__ == "_main_":
    main()