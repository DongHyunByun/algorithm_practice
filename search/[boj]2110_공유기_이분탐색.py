import sys

N,C=map(int,input().split())
L=[]
diff=[]

for i in range(N):
    a=int(sys.stdin.readline())
    L.append(a)
L.sort()

for i in range(1,N):
    diff.append(L[i]-L[i-1])



def cnt_share(min_len):
    '''
    최소거리가 min_len일때 공유기의 최대설치개수
    '''
    cnt=1
    last_loc=L[0]
    for i in range(1,N):
        if min_len<=L[i]-last_loc:
            cnt+=1
            last_loc=L[i]
    return cnt

# print(cnt_share(4))

bot=1
top=L[-1]-L[0]+1
while(bot<top):
    mid = (bot+top)//2

    if cnt_share(mid) <= C-1:
        top=mid
    else:
        bot=mid+1

print(bot-1)


