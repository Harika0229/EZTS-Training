class QueueUsingStacks:
    def _init_(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            raise IndexError("dequeue from empty queue")
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def size(self):
        return len(self.stack1) + len(self.stack2)

queue = QueueUsingStacks()
while True:
    print("\n1. insert\n2. delete\n3. size\n4. display\n5. exit")
    ch=int(input())
    if ch==1:
        n=int(input("enter element: "))
        queue.enqueue(n)
    elif ch==2:
        print(queue.dequeue())
    elif ch==3:
        print(queue.size())
    elif ch==4:
        print(queue.stack1,queue.stack2)
    elif ch==5:
        break

