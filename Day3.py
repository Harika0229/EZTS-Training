#Valid message as prime number
m=int(input("Enter the message:"))
flag=0
if m<0 or m==0:
    flag=1
elif m==1:
    flag=0
else:
    for i in range(2,(m//2)+1):
        if m%i==0:
            flag=1
            break
if flag==1:
    print("Invalid message.")
else:
    print("Valid message")
    
    
#FIbonacci series    
n=int(input("Enter the number:"))        
a=0
b=1
c=a+1
if n==1:
    print(b)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n):
        a=b
        b=c
        c=a+b
        print(c)
        

#Alice of numeria and the prime number
def check_prime(m):
    flag=0
    if m<0 or m==0:
        flag=1
    elif m==1:
        flag=0
    else:
        for i in range(2,(m//2)+1):
            if m%i==0:
                flag=1
                break
    if flag==1:
        return 0
    else:
        return 1
    
N=int(input("Enter the prime number N:"))
flag=0
result=[]
k=N+1    
while flag<1:
    flag=check_prime(k)
    if flag==1:
        result.append(k)
    else:
        k=k+1
sum=0
for i in range(N+1,k):
    sum=sum+i
result.append(sum)

p1=k
flag=0
k=p1+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1 
p3=p1*p2
flag=check_prime(p3)
if flag==0:
    result.append(False)
else:
    result.append(True)
                
Prime_key=tuple(result)
print(Prime_key)

#Max and the diwali contest
cnt=0
time=0
p=int(input("Enter the minutes taken to reach the destination:"))
mins_rem=240-p
for i in range(mins_rem):
    prd=5*i
    time=time+prd
    if prd in range(mins_rem-time):
        cnt=cnt+1
print("Number of problems he can solve:",cnt)
