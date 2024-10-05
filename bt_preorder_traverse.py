def preorder_traversal(root):
    result = []

    def traverse(node):
        if node:
            result.append(node.val)  # Visit root
            traverse(node.left)      # Visit left subtree
            traverse(node.right)     # Visit right subtree
    
    traverse(root)
    return result
