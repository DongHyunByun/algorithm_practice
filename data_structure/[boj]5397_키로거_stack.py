from collections import deque

T=int(input())
for t in range(T):
    stack1=deque([])
    stack2=deque([])
    word=input()
    size=len(word)
    for i in range(size):
        c=word[i]
        if c=="<":
            if stack1:
                stack2.append(stack1.pop())
        elif c==">":
            if stack2:
                stack1.append(stack2.pop())
        elif c=="-":
            if stack1:
                stack1.pop()
        else:
            stack1.append(c)
    ans=""
    while(stack1):
        ans+=stack1.popleft()
    while(stack2):
        ans+=stack2.pop()
    print(ans)