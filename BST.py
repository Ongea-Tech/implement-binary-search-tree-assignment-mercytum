class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.info)

class BinarySearchTree:
    def __init__(self):
        self.root = None

     
    
    def insert(self, value):
        """Insert a value into the BST."""
        pass  # TODO: Implement this method
    
    def search(self, value):
        """Search for a value in the BST. Return True if found, else False."""
        pass  # TODO: Implement this method
    
    def inorder_traversal(self):
        """Return a list of values representing in-order traversal."""
        pass  # TODO: Implement this method
    
    def preorder_traversal(self):
        """Return a list of values representing pre-order traversal."""
        pass  # TODO: Implement this method
    
    def postorder_traversal(self):
        """Return a list of values representing post-order traversal."""
        pass  # TODO: Implement this method
    
    def delete(self, value):
        """Delete a value from the BST."""
        pass  # TODO: Implement this method
    
# Example usage:
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# bst.insert(15)
# print(bst.search(10))  # Expected output: True
# print(bst.inorder_traversal())  # Expected output: [5, 10, 15]
