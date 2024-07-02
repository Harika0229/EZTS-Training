# leetcode-94,104,102,144,145,41,53
#53-maximum sumarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=0
        max_sum=float('-inf')
        n=len(nums)
        for i in range(n):
            curr_sum +=nums[i]
            max_sum=max(max_sum,curr_sum)
            if curr_sum<0:
                curr_sum=0
        return max_sum
#94-binary tree inorder traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return(res)
#145-binary tree postorder traversal
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def postorder(root):
            if root==None:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return(res)
#102
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Q=[root]
        l=[]
        currl=[]
        Q.append(None)
        while Q:
            curr=Q.pop(0)
            if curr==None:
                l.append(currl)
                if len(Q)==0:
                    return l
                else: 
                    currl=[]
                    Q.append(None)
            else:
                currl.append(curr.val)
                if curr.left:
                    Q.append(curr.left)
                if curr.right:
                    Q.append(curr.right)
        return l