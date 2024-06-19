#Repetition of vowels in their sentences
def count_vowels(str):
    dict={'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in str:
        if i.lower()=='a':
            dict['a']+=1
        if i.lower()=='e':
            dict['e']+=1
        if i.lower()=='i':
            dict['i']+=1
        if i.lower()=='o':
            dict['o']+=1
        if i.lower()=='u':
            dict['u']+=1
    x=max(dict.values())
    result=[]
    for i,j in dict.items():
        if j==x:
           result.append(i)
           return result
            
i_p=[
    ["Alex","I enjoy hiking in the mountains"],
    ["Sam","A lovely sunny day at the beach"],
    ["Jamie","Reading a book is my favourite pastime"],
    ["Taylor","I love playing video games on weekends"],
    ["Chris","Exploring the cities is exciting and fun"],
]

o_p={}
for i in i_p:
    o_p[i[0]]=count_vowels(i[1])
print(o_p)

#Equilibrium gate foe treasure hunt
lst=[2,2,1,2,1]
leftSum=0
rtSum=0
for i in range(len(lst)):
    j=i-1
    for k in range(i,len(lst)):
        rtSum=rtSum+lst[k]
        print(rtSum)
    for l in range(0,i):
        leftSum=leftSum+lst[l]
        print(leftSum)
        
#Maximum sub array of 3 continious digits
lst=[2,4,3,5,6,3,4,6,7,1,2,5]
max=0
for i in range(0,len(lst)-2):
    sum=lst[i]+lst[i+1]+lst[i+2]
    if sum>max:
        max=sum
        pos=i
print(lst[pos],lst[pos+1],lst[pos+2])

#Maximum sub array of k continuous digits
lst=[2,3,4,5]
sum=max=0
k=int(input("Number of terms:"))
for i in range(0,len(lst)-k):
    for j in range(k):
        sum=lst[i+j]
    if sum>max:
        max=sum
        pos=i
for j in range(0,k):
    print(lst[pos+j])
    
#Matching the cards after how many picks
input=[3,4,2,4,7]
ls=[]
cnt=0
for i in input:
    if i not in ls:
        ls.append(i)
        cnt+=1
    else:
        break
print(cnt+1)
print(ls)
