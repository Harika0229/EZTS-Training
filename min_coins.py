# available coins= 1,5,7
# bill amount=18
# what will be the minimum number of coins required to pay the bill.


# GREEDY APPROACH

'''
coins=[1,5,7]
amt=18
res={1:0,5:0,7:0}
while amt>0:
    #sorting list in reverse
    m=coins.pop(coins.index(max(coins)))                   
    c=amt//m
    res[m]+=c
    amt=amt%m
print(res)
'''

#-----------------------------------------------------------------------------------------
# DYNAMIC PROGRAMMING

def calculate(coins,amt):

    res=[float('inf')]*(amt+1)
    res[0]=0

    for i in range(1,amt+1):
        for co in coins:
            if i-co>=0:
                res[i]=min(res[i],res[i-co]+1) 
        print(res)
    print("\n")  
    return res[amt] if res[amt]!=float('inf') else -1

coins=[1,5,7]
amt=18
print(calculate(coins,amt))

