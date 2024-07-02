graph = [
    [0, 4, -1, -1, -1, -1, -1, 8, -1],  # 0
    [4, 0, 8, -1, -1, -1, -1, 11, -1],  # 1
    [-1, 8, 0, 7, -1, 4, -1, -1, 2],    # 2
    [-1, -1, 7, 0, 9, 14, -1, -1, -1],  # 3
    [-1, -1, -1, 9, 0, 10, -1, -1, -1], # 4
    [-1, -1, 4, 14, 10, 0, 2, -1, -1],   # 5
    [-1, -1, -1, -1, -1, 2, 0, 1, 6],   # 6
    [8, 11, -1, -1, -1, -1, 1, 0, 7],   # 7
    [-1, -1, 2, -1, -1, 2, 6, 7, 0]   # 8
]
value={0:float('inf'),1:float('inf'),2:float('inf'),3:float('inf'),4:float('inf'),5:float('inf'),
       6:float('inf'),7:float('inf'),8:float('inf')}
res=[0]*len(value)
visit=[False]*len(value)
start=0
value[start]=0
n=len(value)
while False in visit:
    min_key=min(value,key=value.get)
    min_value=value[min_key]
    value.pop(min_key)
    res[min_key]=min_value
    visit[min_key]=True
    for i in range(n):
        if i in value.keys():
            if graph[min_key][i]<=0:
                continue
            elif min_value+graph[min_key][i]<=value[i]:
                    value[i]=min_value+graph[min_key][i]
print(res)
