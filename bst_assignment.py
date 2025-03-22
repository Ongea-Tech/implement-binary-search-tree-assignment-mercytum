class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.root = None

     
    
    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = TreeNode(value)
            
        else:
            self.insert_helper(self.root, value)    
    
    def insert_helper(self, node, value):
        """Helper method for inserting a value into the BST."""
        #value is smaller than root and will be put in the left part of the tree
        if node.value > value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert_helper(node.left, value)
        #value is larger than root and will be put in the right part of the tree
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert_helper(node.right, value)

    def search(self, value):
        """Search for a value in the BST. Return True if found, else False."""
        if self.root == value:
            return True
        
        else:
            return self.search_helper(self.root, value)

    def search_helper(self, node, value):
        if node is None:
            return False
        if node.value ==  value:
            return True
   
        elif node.value > value:
            return self.search_helper(node.left, value)
        else:
            return self.search_helper(node.right, value)
        
    
    def inorder_traversal(self):
        """Return a list of values representing in-order traversal."""
        result = []
        # If the root is None, return an empty list
        if self.root is None:
            return result
        # If the root is not None, we have already added its value
        self.inorder_traversal_helper(self.root, result)
        return result
    
    def inorder_traversal_helper(self, node, output):
        """Helper method for in-order traversal."""
        if node:
            self.inorder_traversal_helper(node.left, output)
            output.append(node.value)
            self.inorder_traversal_helper(node.right, output)
    
    def preorder_traversal(self):
        """Return a list of values representing pre-order traversal."""
        result = []
        # If the root is None, return an empty list
        if self.root is None:
            return result
        # If the root is not None, we have already added its value
        self.preorder_traversal_helper(self.root, result)
        return result
    
    def preorder_traversal_helper(self, node, output):
        """Helper method for pre-order traversal."""
        if node:
            output.append(node.value)
            self.preorder_traversal_helper(node.left, output)
            self.preorder_traversal_helper(node.right, output)
    
    def postorder_traversal(self):
        """Return a list of values representing post-order traversal."""
        result = []
        # If the root is None, return an empty list
        if self.root is None:
            return result
        # If the root is not None, we have already added its value
        self.postorder_traversal_helper(self.root, result)
        return result
    
    def postorder_traversal_helper(self, node, output):
        if node:
            self.postorder_traversal_helper(node.left, output)
            self.postorder_traversal_helper(node.right, output)
            output.append(node.value)

        

    def delete(self, value):
        """Delete a value from the BST."""
        pass  # TODO: Implement this method
    
# Example usage:
bst = BinarySearchTree()
bst.insert(6)
bst.insert(10)
bst.insert(5)
bst.insert(15)
print(bst.search(10))  # Expected output: True
print(bst.inorder_traversal())  # Expected output: [5, 10, 15]
print(bst.preorder_traversal())  # Expected output: [10, 5, 15]
print(bst.postorder_traversal())