class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
class LinkedList:
    Head=None
    Tail=None
    size=0
    def print_list(self):
        if self.Head==None:
            print("List is empty")
        else:
            cur=self.Head
            while cur!=None:
                print(cur.value)
                cur=cur.next
                
    def InsF(self,data):
        temp=Node(data)
        if self.Head==None:
            self.Head=self.Tail=temp
        else:
            temp.next=self.Head
            self.Head=temp
        self.size+=1
            
    def InsE(self,data):
        temp=Node(data)
        if self.Head==None:
            self.Tail=self.Head=temp
        else:
            cur=self.Head
            while cur.next!=None:
                cur=cur.next
            cur.next=temp
        self.size+=1
        
    def InsM(self,data,pos):
        temp=Node(data)
        if self.Head==None:
            self.Head=self.Tail=temp
        else:
            cur=self.Head
            while cur.value!=pos:
                cur=cur.next
            temp.next=cur.next
            cur.next=temp
        self.size+=1
    
    def deleF(self):
        if self.Head==None:
            print("List is empty")
        else:
            cur=self.Head
            self.Head=self.Head.next
            cur.next=None
        self.size=self.size-1
        
    def deleE(self):
        if self.Head==None:
            print("List is empty")
        else:
            cur=self.Head
            while cur.next!=None:
                temp=cur
                cur=cur.next
            temp.next=None
        self.size=self.size-1
        
    def deleM(self,pos):
        if self.Head==None:
            print("List is empty")
        elif self.Head.value==pos:
            self.Head=self.Head.next    
        else:
            cur=self.Head
            while cur.value!=pos:
                temp=cur
                cur=cur.next
            temp.next=cur.next
            cur.next=None
        self.size=self.size-1
            
            
l=LinkedList()
l.InsF(60)
l.InsF(70)
l.InsE(50)
l.InsF(10)
l.InsM(35,60)
l.print_list()
l.deleE()
l.deleM(60)
l.print_list()
l.deleF()
l.print_list()