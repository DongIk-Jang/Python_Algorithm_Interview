def rangeSumBST(root, low, high):
    from collections import deque
    stack = deque([root])
    answer = 0
    while stack:
        node = stack.popleft()
        left = node.left
        right = node.right
        
        if left:
            stack.append(left)
        if right:
            stack.append(right)
            
        if node.val <= high and node.val >= low:
            answer += node.val
            
    return answer