class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
def inorder(root):
    if root==None:
        return 
    inorder(root.left)
    print(root.value)
    inorder(root.right)
        
def insertBST(value,root):
    if root==None:
        root=node(value)
    if value<root.value:
        root.left=insertBST(value,root.left)
    if value>root.value:
        root.right=insertBST(value,root.right)
    return root
        
lst=[4,6,7,3,8,2,5,9,1]
root=node(lst.pop(0))
for i in lst:
    insertBST(i,root)
inorder(root)