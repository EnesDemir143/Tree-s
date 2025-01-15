class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.value:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    def search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self.search(root.left, key)
        return self.search(root.right, key)
    
    def remove(self, root, key):
        # Case 1: If the tree is empty
        if root is None:
            return root
        
        # Case 2: Traverse the tree to find the node to be deleted
        if key < root.value:
            root.left = self.remove(root.left, key)
        elif key > root.value:
            root.right = self.remove(root.right, key)
        else:
            # Case 3: Node to be deleted is found

            # Case 3a: Node has no children (leaf node)
            if root.left is None and root.right is None:
                return None
            
            # Case 3b: Node has one child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3c: Node has two children
            else:
                # Find the inorder successor (smallest in the right subtree)
                min_larger_node = self.get_minimum(root.right)
                root.value = min_larger_node.value  # Replace value with the successor's value
                root.right = self.remove(root.right, min_larger_node.value)  # Remove the successor

        return root

    def get_minimum(self, root):
        current = root
        while current.left:
            current = current.left
        return current


# Example Usage:
bst = BST()
root = None
root = bst.insert(root, 50)
root = bst.insert(root, 30)
root = bst.insert(root, 20)
root = bst.insert(root, 40)
root = bst.insert(root, 70)
root = bst.insert(root, 60)
root = bst.insert(root, 80)

print("In-order before deletion:")
bst.inorder(root)
print()

# Remove a node
key_to_remove = 50
root = bst.remove(root, key_to_remove)

print(f"In-order after removing {key_to_remove}:")
bst.inorder(root)
print()