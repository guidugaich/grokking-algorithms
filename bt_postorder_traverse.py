def postorder_traversal(root):
    result = []

    def traverse(node):
        if node:
            traverse(node.left)    # Visit left subtree
            traverse(node.right)   # Visit right subtree
            result.append(node.val)  # Visit root
    
    traverse(root)
    return result
