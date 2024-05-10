

from dataStructure.binaryTree import Optional, TreeNode


class BinaryTreeAlgorithm:
    pass

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def B(temp):
            if temp is None:
                return None
            l = B(temp.left)
            r = B(temp.right)
            #l = l1[:] if l1 else None
            #r = r1[:] if r1 else None
            if l and r:
                return f"{temp.val}({l})({r})"
            elif l and (r is None):
                return f"{temp.val}({l})"
            elif (l is None) and r:
                return f"{temp.val}()({r})"
            else:
                return f"{temp.val}"
        return B(root)
            
                
        