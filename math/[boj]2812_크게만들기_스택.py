from collections import deque

N,K=map(int,input().split())
num=input()
size=len(num)

cut=0

stack=deque([num[0]])
isFull=False
for i in range(1,size):
    intI=int(num[i])
    # 1. 스택에 숫자가 없으면 그만
    while(stack):
        stackNum=stack.pop()
        # 2. 스택에서 뽑은 숫자가 i번째 숫자보다 크거나 같을때
        if int(stackNum)>=intI:
            stack.append(stackNum)
            break
        cut+=1
        # 3. 지울 수 있는 횟수를 다 썼을때
        if cut==K:
            isFull=True
            break

    if isFull:
        stack.extend(num[i:])
        break
    else:
        stack.append(num[i])


ans="0"+"".join(list(stack)[:N-K])
print(int(ans))


