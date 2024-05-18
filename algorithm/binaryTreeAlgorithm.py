
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
            if not temp:
                return
            # Begin A
            # End A
            B(temp.left)
            # Begin B
            ans.append(temp.val)
            # End B
            B(temp.right)
            # Begin C
            # End C

        B(root)
        return ans
    
    def binaryTreeToInorderTraversal(self, root):
        temp = root
        stack = []
        ans = []

        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left
            
            temp = stack.pop()
            # Begin B
            ans.append(temp.val)
            # End B
            temp = temp.right
        
        return ans  
               
    def binaryTreeToPreorderTraversal(self, root):
        ans = []
        def B(temp):
            if not temp:
                return 
            ans.append(temp.val)
            B(temp.left)
            B(temp.right)
        B(root)
        return ans  

    def binaryTreeToPreorderTraversal(self, root):
        ans = []
        stack = [root]
        
        while stack:
            temp = stack.pop()
            if temp:
                ans.append(temp.val)
                stack.append(temp.right)
                stack.append(temp.left)
        return ans              
    
    def binaryTreeToPostorderTraversal(self, root):
        ans = []
        def B(temp):
            if not temp:
                return
            B(temp.left)
            B(temp.right)
            ans.append(temp.val)
        B(root)
        return ans

    def binaryTreeToPostorderTraversal(self, root):
        
        # Base case...
        if not root:
            return []
        
        # Create an array list to store the solution result...
        ans = []
        
        # Create an empty stack and push the root node...
        stack = [root]
        
        # Loop till stack is empty...
        while stack:
            
            # Pop a node from the stack...
            temp = stack.pop()
            ans.append(temp.val)
            
            # Push the left child of the popped node into the stack...
            if temp.left:
                stack.append(temp.left)
                
            # Append the right child of the popped node into the stack...
            if temp.right:
                stack.append(temp.right)
                
        return ans[::-1]       # Return the solution list...
    
    def arithmeticOperations(self, oper1, oper2, oper):
        if oper == "*":
            return oper1 * oper2
        if oper == "/":
            return oper1 / oper2
        if oper == "+":
            return oper1 + oper2
        if oper == "-":
            return oper1 - oper2
        
    def F(self, nums):
        stack = []
        for e in nums:
            if type(e) == str:
                oper2 = stack.pop()
                oper1 = stack.pop()
                stack.append(self.arithmeticOperations(oper1, oper2, e))
            else:
                stack.append(e)
        return stack[-1]
    
    def maximumDepthOfBinaryTree(self, root) -> int:
      
        ans = [0]
        
        def B(temp, depth):
            
            if not temp: 
                return
            B(temp.left, depth + 1)
            B(temp.right, depth + 1)
            x = ans.pop()
            ans.append(max(x, depth))
                       
        B(root, 1)
        return ans[0]
        




def main():
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    algo = BinaryTreeAlgorithm()

    nums = [4, 7, 2, "-", "*", 5, "*"]
    print(algo.F(nums))

    # x = 20
    # y = 5
    # print("{} * {} = {}".format(x, y, algo.arithmeticOperations(x, y, "*")))
    # print("{} / {} = {}".format(x, y, algo.arithmeticOperations(x, y, "/")))
    # print("{} + {} = {}".format(x, y, algo.arithmeticOperations(x, y, "+")))
    # print("{} - {} = {}".format(x, y, algo.arithmeticOperations(x, y, "-")))
    
    # print()
    # print("================= Begin ====================================")
    # print("Binary Tree To Str: ", algo.binaryTreeToStr(root), end="\n\n")
    # print("Inorder Traversal: ", algo.binaryTreeToInorderTraversal(root))
    # print("Preorder Traversal: ", algo.binaryTreeToPreorderTraversal(root))
    # print("Postorder Traversal: ", algo.binaryTreeToPostorderTraversal(root))

if __name__ == "__main__":
    main()
        