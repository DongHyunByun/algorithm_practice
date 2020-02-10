import math
N,M,K=map(int,input().split())
# 여자가 남음
if N>=2*M:
    over=N-2*M
    isOverWo=True
# 남자가 남음
elif N<2*M:
    if N%2==0:
        over=M-N//2
    else:
        over=M-N//2+1
    M=N//2
    isOverWo=False

if over>=K:
    print(M)
else:
    K-=over
    needTeem=math.ceil(K/3)
    ans=M-needTeem
    if ans>=0:
        print(ans)
    else:
        print(0)