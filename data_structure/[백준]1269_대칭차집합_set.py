a,b=map(int,input().split())

A=set(list(map(int,input().split())))
B=set(list(map(int,input().split())))

subA=A-B
subB=B-A

print(len(subA)+len(subB))