from collections import deque
first=["*","/"]
second=["+","-"]

A=input()
size=len(A)
stack=deque([])
ans=""

for i in A:
    # 괄호
    if i==")":
        while(stack):
            temp=stack.pop()
            if temp=="(":
                break
            else:
                ans+=temp
    elif i=="(":
        stack.append("(")
    # 곱셈 나눗셈?
    elif i in first:
        while(stack):
            temp=stack.pop()
            if temp in first:
                ans+=temp
            else:
                stack.append(temp)
                break
        stack.append(i)
    # 덧셈 뺄셈?
    elif i in second:
        while(stack):
            temp=stack.pop()
            if temp in first or temp in second:
                ans+=temp
            else:
                stack.append(temp)
                break
        stack.append(i)
    else:
        ans+=i

while(stack):
    ans+=stack.pop()

print(ans)





