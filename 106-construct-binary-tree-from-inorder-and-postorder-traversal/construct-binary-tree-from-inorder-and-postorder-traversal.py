# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        

        self.idx=len(postorder)-1
        inorder_map={val:idx for idx, val in enumerate(inorder)}
# heading
        def traversal(left,right):

            if left>right:

                return None

            node_val=postorder[self.idx]
            root=TreeNode(node_val)
            self.idx-=1

            splitter = inorder_map[node_val]

            root.right=traversal(splitter+1,right)
            root.left=traversal(left,splitter-1)

            return root
        return traversal(0,len(inorder)-1)


            
        