#AVL tree
class node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.height=1
        
def inorder(root):
    if not root:
        return
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
def ght(root):
    if not root:
        return 0
    return root.height

def getBF(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)
        
def leftRotate(A):
    B=A.right
    temp=B.left
    B.left=A
    A.right=temp
    A.height= ght(A.left)-ght(A.right)
    B.height= ght(B.left)-ght(B.right)
    getBF(A)
    getBF(B)
    return B

def rightRotate(A):
    B=A.left
    temp=B.right
    B.right=A
    A.left=temp
    A.height= ght(A.left)-ght(A.right)
    B.height= ght(B.left)-ght(B.right)
    getBF(A)
    getBF(B)
    return B
        
def insert(root,bitm):
    if not root:
        return node(bitm)
    if bitm<root.val:
        root.left=insert(root.left,bitm)
    else:
        root.right=insert(root.right,bitm)
        
    root.height=1+max(ght(root.left),ght(root.right))
    
    BF=getBF(root)
    #RR rotation
    if BF>1 and bitm<root.left.val:
        return rightRotate(root)
    
    #RL rotation
    if BF>1 and bitm>root.left.val:
        root.left=leftRotate(root.left)
        return rightRotate(root)
    
    #LL Rotation
    if BF<-1 and bitm>root.right.val:
        return leftRotate(root)
    
    #LR rotation
    if BF<-1 and bitm<root.right.val:
        root.right=rightRotate(root.right)
        return leftRotate(root)
    
    return root
    

if __name__=="__main__":
    root=None
    VL=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in VL:
        root=insert(root,i)
    inorder(root)
    
    
#Problems   
#Counting the number of commas needed to print the numbers from 1000 to 100,000
cnt=0
for i in range(1000,100001):
    cnt+=1
print(cnt)

#Least positive integer
lst=[6,-7,1,8,3,-9,0,2]
Plst=[]
for i in lst:
    if i>0:
        Plst.append(i)
#print(Plst)
min=Plst[0]
for  i in Plst:
    if i<min:
        min=i
print(min)

#Missing positive integer
def func(lst):
    if 1 not in lst:
        return 1
    else:
        for i in range(1,maxi):
            if i not in lst:
                return i
                break
lst=[1,2,-1]
maxi=max(lst)
#print(maxi)
print(func(lst))
        
    