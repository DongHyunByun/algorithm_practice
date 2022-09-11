import sys

N,M=map(int,input().split())
L=list(map(int,sys.stdin.readline().split()))

def cnt_blue(max_len):
    now_len=0
    cnt_blue=1

    for size in L:
        if max_len<size+now_len:
            now_len=size
            cnt_blue+=1
        else:
            now_len+=size

    return cnt_blue

def lower_bound(target):
    top = sum(L)
    bot = max(L)

    while(bot<top):
        mid = (bot+top)//2
        # print(bot, mid,top)
        if target < cnt_blue(mid):
            bot = mid+1
        else:
            top = mid

    print(bot)

def upper_bound(target):
    top = sum(L)+1
    bot = max(L)

    while(bot<top):
        mid = (bot+top)//2
        if target+1<=cnt_blue(mid):
            bot = mid+1
        else:
            top = mid

    print(bot)

upper_bound(M)
# lower_bound(M)
