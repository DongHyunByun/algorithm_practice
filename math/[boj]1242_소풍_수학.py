N,K,M=map(int,input().split())

indx=0
size=N
dongho=M-1
ans=1
while(1):
    #이동!
    indx=(indx+K-1)%size
    #삭제!
    if indx<dongho:
        dongho-=1
    elif indx==dongho:
        break
    size-=1
    #정답!
    ans+=1
print(ans)
