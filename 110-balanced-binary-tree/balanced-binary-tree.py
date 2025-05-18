class Solution(object):
    def isBalanced(self, root):
        def check_balance(node):
            if not node:
                return 0
            left = check_balance(node.left)
            if left == -1:
                return -1
            right = check_balance(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return check_balance(root) != -1