
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeAlgorithm:


    def binaryTreeToStr(self, root) -> str:
        
        def B(temp):
            if temp is None:
                return None
            
            l = B(temp.left)
            r = B(temp.right)
            
            if l and r:
                return f"{temp.val}({l})({r})"
            elif l and (r is None):
                return f"{temp.val}({l})"
            elif (l is None) and r:
                return f"{temp.val}()({r})"
            else:
                return f"{temp.val}"
            
        return B(root)
            
    def binaryTreeToInorderTraversal(self, root):
        ans = []
        def B(temp):
            if temp:
                B(temp.left)
                ans.append(temp.val)
                B(temp.right)
        B(root)
        return ans
               
    def binaryTreeToPreorderTraversal(self, root):
        ans = []
        def B(temp):
            if temp:
                ans.append(temp.val)
                B(temp.left)
                B(temp.right)
        B(root)
        return ans                
    
    def binaryTreeToPostorderTraversal(self, root):
        ans = []
        def B(temp):
            if temp:
                B(temp.left)
                B(temp.right)
                ans.append(temp.val)
        B(root)
        return ans



def main():
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    algo = BinaryTreeAlgorithm()
    
    print()
    print("================= Begin ====================================")
    print("Binary Tree To Str: ", algo.binaryTreeToStr(root), end="\n\n")
    print("Inorder Traversal: ", algo.binaryTreeToInorderTraversal(root))
    print("Preorder Traversal: ", algo.binaryTreeToPreorderTraversal(root))
    print("Postorder Traversal: ", algo.binaryTreeToPostorderTraversal(root))

if __name__ == "__main__":
    main()
        