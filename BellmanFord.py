G=[
    [0,6,4,5,False,False],
    [False,0,False,False,-1,False],
    [False,-2,0,False,3,False],
    [False,False,-2,0,False,-1],
    [False,False,False,0,False,3],
    [False,False,False,False,False,0]
]
E_L=[]
d={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F'}
for i in range(len(G)):
    for j in range(len(G[i])):
        if G[i][j]!=False and G[i][j]!=0:
            E_L.append(tuple((i,j)))
            
print(E_L)
dist={}
for i in range(len(G)):
    dist[i]=float("inf")
dist[0]=0
#print(dist)
for i in range(len(G)-1):
    for j in E_L:
        new_dist=dist[j[0]]+G[j[0]][j[1]]
        if dist[j[1]]>new_dist:
            dist[j[1]]=new_dist
            
print(dist)
