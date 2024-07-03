# knapsack using "RECURSION METHOD"

'''p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
ratio={}
for i in range(len(p)):
    ratio[i]=p[i]/w[i]
print(ratio)
l=list(ratio.items())
print(i)

# b=lambda x:1[x][1]
# print(b(2))

# Sorting by using lambda function

# method 1 by using sort()
l.sort(key=lambda x:x[1],reverse=True)
print(l)

# method 2 by using sorted()
sorted_list=sorted(l,key=lambda x:x[1],reverse=True)
print(sorted_list)

# Sorting without using lambda

n=len(l)
for i in range(n-1):
    max=i
    for j in range(i+1,n):
        if l[j][1]>l[max][1]:
            max=j
    l[i],l[max]=l[max],l[i]
sorted_ratio={}
for i in l:
    sorted_ratio[i[0]]=i[1]
print(sorted_ratio)
knap_sack=8'''



#----------------------------------------------------------------------------------------------------

# RECURSION METHOD

def calc_max(p,w,c,n):
    if n==0 or c==0:
        return 0
    if w[n-1]>c:
        return calc_max(p,w,c,n-1)
    else:
        return max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))

c=15
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
n=len(p)
max_profit=calc_max(p,w,c,n)
print(max_profit)

#----------------------------------------------------------------------------------------------------

# Knapsack using dynamic programming - "MEMORIZATION METHOD"

# Memorization : Recursion + Data storage

def calc_max(p,w,c,n):
    if n==0 or c==0:
        return 0
    if dp[n][c]!=-1:
        return dp[n][c]
    if w[n-1]<=c:
        dp[n][c]=max(p[n-1]+calc_max(p,w,c-w[n-1],n-1),calc_max(p,w,c,n-1))
        return dp[n][c]
    else:
        dp[n][c]=calc_max(p,w,c,n-1)
        return dp[n][c]

c=15
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
n=len(p)
dp=[[-1 for i in range(c+1)] for j in range (n+1)]
max_profit=calc_max(p,w,c,n)
for i in dp:
    print(i)
print(max_profit)


#---------------------------------------------------------------------------------------------------

# knapsack using "TABULATION METHOD"

# def cal_max(p,w,c,n):
#     for i in range(1,n+1):
#         for j in range(1,c+1):
#             if j-w[i-1]<0:
#                 dp[i][j]=dp[i-1][j]
#             else:
#                 dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])
#     return dp[n][c]


c=15
p=[5,10,15,7,8,9,4]
w=[1,3,5,4,1,3,2]
n=len(p)
dp=[[0 for i in range(c+1)] for j in range (n+1)]
for i in range(1,n+1):
    for j in range(1,c+1):
        if j-w[i-1]<0:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],p[i-1]+dp[i-1][j-w[i-1]])
for i in dp:
    print(i)
print(dp[n][c])
