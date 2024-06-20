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
    
def postorder(root):
    if root==None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.value)
    
def preorder(root):
    if root==None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)
    
def levelorder(root):
    Q=[root]
    Q.append(None)
    while len(Q)>0:
        curr=Q.pop(0)
        if curr==None:
            if len(Q)==0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                Q.append(curr.left)
            if curr.right!=None:
                Q.append(curr.right)
                
def height(root):
    if root==None:
        return 0
    LH=height(root.left)
    RH=height(root.right)
    return max(LH,RH)+1
 
def leafnodes(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        print(root.value)
    leafnodes(root.left)
    leafnodes(root.right)

if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(8)
    root.left.right.right=node(9)
    root.right.right.right=node(10)
    root.left.right.left.left=node(11)
    root.left.right.left.right=node(12)
    
    print("Preorder")
    preorder(root)
    print("Inorder")
    inorder(root)
    print("Postorder")
    postorder(root)
    print("BFS of the tree:")
    levelorder(root)
    print("Height of the tree:")
    print(height(root))
    print("Leaf nodes of the tree:")
    leafnodes(root)
