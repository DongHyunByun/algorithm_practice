from collections import deque

N=int(input())
L=list(input())
pointer=0
cal=["*","/","+","-"]
size=len(L)

def calculate(a,b,c):
    if c=="*":
        return a*b
    elif c=="/":
        return a/b
    elif c=="+":
        return a+b
    else:
        return a-b

for i in range(N):
    num=int(input())
    alpa=chr(65+i)
    for j in range(size):
        if L[j]==alpa:
            L[j]=num

stack=deque([])
for i in range(size):
    temp=L[i]
    if temp in cal:
        b=stack.pop()
        a=stack.pop()
        stack.append(calculate(a,b,L[i]))
    else:
        stack.append(temp)

print("%.2f"%(stack[0]))
