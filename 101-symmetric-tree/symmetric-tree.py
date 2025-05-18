from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        queue = deque([(root, root)])

        while queue:
            t1, t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True