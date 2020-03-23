import sys

N=int(input())

L=[]
for i in range(N):
    name,state=(sys.stdin.readline().rstrip()).split(" ")
    if state=="enter":
        L.append(name)
    else:
        L.remove(name)

L.sort(reverse=True)

for i in L:
    print(i)