import sys

sys.setrecursionlimit(10 ** 7)

k = int(input())
turn = [1, 0]


def cheak():
    for v in range(1, V + 1):
        nowColor = colorV[v]
        for conNode in graph[v]:
            if colorV[conNode] == nowColor:
                print("NO")
                return
    print("YES")


def dfs(node):
    color = colorV[node]
    for conNode in graph[node]:
        if colorV[conNode] == -1:
            colorV[conNode] = turn[color]
            dfs(conNode)


for t in range(k):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    graph = {}
    for i in range(1, V + 1):
        graph[i] = []
    a=0
    for i in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    # 색 칠하기
    colorV = [-1 for i in range(V + 1)]
    for i in range(1,V+1):
        if colorV[i]==-1:
            colorV[i] = 1
            dfs(i)
    # print(colorV)
    # 확인하기
    cheak()