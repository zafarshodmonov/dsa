
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeAlgorithm:

    def F106Y(self, ino: list[int], post: list[int]):
        root = post[-1]
        if len(post) == 1:
            return root, [], [], [], []
        
        ele = post[-1]
        ind = ino.index(ele)
        A = (ind == 0)
        B = (ind == len(ino) - 1)
        if A and B:
            pass
        elif A and not B:
            re_ch_ino = []
            re_ch_post = []
            re_on_ino = ino[ind+1:]
            re_on_post = post[:-1]
            return root, re_ch_ino, re_ch_post, re_on_ino, re_on_post
        elif not A and B:
            re_ch_ino = ino[:ind]
            re_ch_post = post[:-1]
            re_on_ino = 0
            re_on_post = 0
            return root, re_ch_ino, re_ch_post, re_on_ino, re_on_post
        else:
            re_ch_ino = ino[:ind]
            re_ch_post = post[:ind]
            re_on_ino = ino[ind+1:]
            re_on_post = post[ind:-1]
            return root, re_ch_ino, re_ch_post, re_on_ino, re_on_post

    def inPostToBinaryTree(self, inorder: list[int], postorder: list[int]):
        def B(ino, post):
            if not post:
                return None
            res = self.F106Y(ino, post)
            l = B(res[1], res[2])
            r = B(res[3], res[4])
            return TreeNode(res[0], l, r)
        return B(inorder, postorder)

    def constructFromPrePostF(self, pre: list[int], post: list[int]):
        if len(pre) == 1:
            return pre[0], [], [], [], []
        ele = pre[1]
        ind = post.index(ele)
        B = (ind == len(post) - 2)
        if B:
            re_ch_pre = []
            re_ch_post = []
            re_on_pre = pre[1:]
            re_on_post = post[:-1]
            return pre[0], re_ch_pre, re_ch_post, re_on_pre, re_on_post
        re_ch_pre = pre[1:ind+2]
        re_ch_post = post[:ind+1]
        re_on_pre = pre[ind+2:]
        re_on_post = post[ind+1:-1]
        return pre[0], re_ch_pre, re_ch_post, re_on_pre, re_on_post

    def prePostToBinaryTree(self, preorder: list[int], postorder: list[int]):
        def B(pre, post):
            if not pre:
                return None
            res = self.constructFromPrePostF(pre, post)
            l = B(res[1], res[2])
            r = B(res[3], res[4])
            return TreeNode(res[0], l, r)
        return B(preorder, postorder)
        
    def preInToBinaryTreeY(self, pre: list[int], ino: list[int]):

        root_val = pre[0]
        ind = ino.index(root_val)

        A = (ind == 0)
        B = (ind == len(ino) - 1)

        if A and B:
            re_ch_ino = []
            re_ch_pre = []
            re_on_ino = []
            re_on_pre = []
            return root_val, re_ch_ino, re_ch_pre, re_on_ino, re_on_pre
        elif A and not B:
            re_ch_ino = []
            re_ch_pre = []
            re_on_ino = ino[1:]
            re_on_pre = pre[1:]
            return root_val, re_ch_ino, re_ch_pre, re_on_ino, re_on_pre
        elif not A and B:
            re_ch_ino = ino[:-1]
            re_ch_pre = pre[1:]
            re_on_ino = []
            re_on_pre = []
            return root_val, re_ch_ino, re_ch_pre, re_on_ino, re_on_pre
        else:
            re_ch_ino = ino[:ind]
            re_ch_pre = pre[1:ind + 1]
            re_on_ino = ino[ind + 1:]
            re_on_pre = pre[ind + 1:]
            return root_val, re_ch_ino, re_ch_pre, re_on_ino, re_on_pre

    def preInToBinaryTree(self, preorder: list[int], inorder: list[int]):
        def B(pre, ino):
            if not pre:
                return None
            res = self.preInToBinaryTreeY(pre, ino)
            l = B(res[2], res[1])
            r = B(res[4], res[3])
            return TreeNode(res[0], l, r)
        return B(preorder, inorder)
    

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
    algo = BinaryTreeAlgorithm()

    # Input
    str_tree = "1(2(4(7))(6()(9)))(3(21)(5()(10)))"
    inorder = [7, 4, 2, 6, 9, 1, 21, 3, 5, 10]
    preorder = [1, 2, 4, 7, 6, 9, 3, 21, 5, 10]
    postorder = [7, 4, 9, 6, 2, 21, 10, 5, 3, 1]

    # Processing
    root = algo.preInToBinaryTree(preorder, inorder)

    # Output
    print("Str: ", algo.binaryTreeToStr(root))
    print("Inorder: ", algo.binaryTreeToInorderTraversal(root))
    print("Preorder: ", algo.binaryTreeToPreorderTraversal(root))
    print("Postorder: ", algo.binaryTreeToPostorderTraversal(root))


    # root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    

    # nums = [4, 7, 2, "-", "*", 5, "*"]
    # print(algo.F(nums))

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
        