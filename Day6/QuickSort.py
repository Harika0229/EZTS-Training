#Quick Sort
def divide(l,low,high):
    P=l[high]
    Pi=high
    j=low-1
    for i in range(low,high):
        if l[i]<l[high]:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[j],l[Pi]=l[Pi],l[j]
    Pi=j
    return Pi

def QuickSort(l,low,high):
    if low<high:
        Pi=divide(l,low,high)
        #print(Pi,low,high)
        QuickSort(l,low,Pi-1)
        QuickSort(l,Pi+1,high)
    return

if __name__=="__main__":
    l=list(map(int,input("Enter the elements:").split()))
    low=0
    high=len(l)-1
    #print(low,high)
    QuickSort(l,low,high)
    print("Sorted array: ",l)
    