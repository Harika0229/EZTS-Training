#Adjacency list of the graph
G={1:[(1,2,0),(1,3,0)],2:[(2,1,0),(2,7,0)],3:[(3,1,0),(3,5,0),(3,6,0)],4:[(4,7,0),(4,8,0)],5:[(5,3,0),(5,7,0)],6:[(6,3,0),(6,8,0)],7:[(7,2,0),(7,4,0),(7,5,0)],8:[(8,4,0),(8,6,0)]}
#Visited dict
V={1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False}
S=[]#Stack

#Depth first search traversal of a graph
def DFS(G,V,S,E):
    if V[E]==False:
        S.append(E)
        V[E]=True
    else:
        return
    for i in G[E]:
        DFS(G,V,S,i[1])
    print(S.pop())

#Breadth first search of the graph
def BFS(G,e):
    Q=[e]
    V={}
    for i in G.keys():
        V[i]=False
    V[e]=True
    while len(Q)!=0:
        curr=Q.pop(0)
        print(curr)
        for i in G[curr]:
            if V[i[1]]==False:
                Q.append(i[1])
                V[i[1]]=True
#Function call
#Depth first search traveral
DFS(G,V,S,1)
#Breadth first search traversal
BFS(G,1)

