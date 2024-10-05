def inorder_traversal(root):
    result = []

    def traverse(node):
        if node:
            traverse(node.left)    # Visit left subtree
            result.append(node.val)  # Visit root
            traverse(node.right)   # Visit right subtree
    
    traverse(root)
    return result
