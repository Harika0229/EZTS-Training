# s= ABABABCANFKABABCNKABABCACNDA
# p=ABABCA

# return the index of p in s
'''
s='ABABABCANFKABABCNKABABCACNDA'
print(len(s))
p='ABABCA'
print(s.count(p))
st=[]
for i in range(len(s)):
    if p==s[i:i+len(p)]:
        st.append(i)
print(st)
'''

#----------------------------------------------------------------------------------------

# LPS- LONGEST PREFIX AND SUFFIX --> Knuth-Morris-Pratt KMP String Matching Algorithm

'''txt= "ABABACDEABABABCABCCABCABDAA"
pat= "ABCAB"
'''
'''
def lps_array(p):
    lps=[0]
    j=0
    for i in range(1,len(p)):
        if p[i] == p[j]:
            lps.append(j+1)
            j=j+1
        else:
            j=0
            lps.append(j)
    return lps

def kmpalgo(p,s):
    lps=lps_array(p)
    print(lps)
    i=0
    j=0
    n=len(s)-1
    m=len(p)-1
    while (n-i) >= (m-j):
        if p[j] == s[i]:
            i+=1
            j+=1
        if j == m:
            print("pattern found",i-j)
            j=lps[j-1]
        elif i<n and p[j]!=s[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1

if __name__=='__main__':
    s= "ABABACDEABABABCABCCABCABDAA"
    p= "ABCAB"
    kmpalgo(p,s)
'''
#--------------------------------------------------------------------------------------------------
# Type 2

#Longest Prefix and Suffix --> KMP algorithm

#LPS Array 

lps=[0]
s="ABABCABCABCABDAA"
p="ABCAB"
j=0
for i in range(1,len(p)):
    if p[i]==p[j]:
        lps.append(j+1)
        j=j+1
    else:
        j=0
        lps.append(j)
print(lps)

#Loop for finding the pattern index based on the lps array

j=-1
i=0
print(len(s))
while i<(len(s)-1):
    if j==len(p)-1:
        print("index:",i-len(p))
        j=lps[j-1]
    if s[i]==p[j+1]:
        j=j+1
        i=i+1
    elif s[i]!=p[j+1] and i<len(s)-1:
        if j!=0:
            j=lps[j-1]
        else:
            i+=1  

#Finding the pattern without using the lps Array

st=[]
for i in range(len(s)):
    if p==s[i:i+len(p)]:
        st.append(i)
print(st)
