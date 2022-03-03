import sys

sys.setrecursionlimit(10**6)

L=[]
while(1):
    try:
        L.append(int(sys.stdin.readline()))
    except:
        break

root = L[0]
graph={num:[0,0] for num in L}

def dfs(a,b):
    if b<a:
        if graph[a][0]==0:
            graph[a][0]=b
        else:
            dfs(graph[a][0],b)

    else:
        if graph[a][1]==0:
            graph[a][1]=b
        else:
            dfs(graph[a][1],b)

for num in L[1:]:
    dfs(root,num)

def postorder(a):
    if a==0:
        return

    postorder(graph[a][0])
    postorder(graph[a][1])
    print(a)

postorder(root)







