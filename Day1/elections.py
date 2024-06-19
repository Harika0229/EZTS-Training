#To display the candidate with the most number of votes
vote=list(map(int,input("Enter the votes:").split(" ")))#Enter the votes as space separated integers from 1 to 6
count=[0]*6
for i in vote:
    if 1 <= i <= 6:
        count[i-1]=count[i-1]+1
    else:
        print(f"Invalid vote detected: {i}")
print(count)
for i in range(len(count)):
    if count[i]==max(count):
        print(i+1)
        
        
    
