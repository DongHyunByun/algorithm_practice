from collections import deque
rever=["1","0"]

N=int(input())
now=list(input())
to=list(input())

def cheak(now,to):
    copiedNow=list(now)
    cnt=0
    #N-2까지 맞추기
    for i in range(N-2):
        if copiedNow[i]==to[i]:
            continue
        else:
            copiedNow[i]=rever[int(copiedNow[i])]
            copiedNow[i+1]=rever[int(copiedNow[i+1])]
            copiedNow[i+2]=rever[int(copiedNow[i+2])]
            cnt += 1
    #마지막두개 맞추기
    if copiedNow[N-1]!=to[N-1] or copiedNow[N-2]!=to[N-2]:
        cnt+=1
        copiedNow[N-1]=rever[int(copiedNow[N-1])]
        copiedNow[N-2]=rever[int(copiedNow[N-2])]
    #맞는지 확인
    if copiedNow[N-1]==to[N-1] and copiedNow[N-2]==to[N-2]:
        return cnt
    else:
        return -1

#처음꺼안바꾸고
a=cheak(now,to)
if a==-1:
    #처음꺼바꾸고
    now[0]=rever[int(now[0])]
    now[1]=rever[int(now[1])]
    b=cheak(now,to)
    if b==-1:
        print(-1)
    else:
        print(b+1)
else:
    print(a)





