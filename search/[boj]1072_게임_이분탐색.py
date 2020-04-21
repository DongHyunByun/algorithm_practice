while(1):
    try:
        X,Y=map(int,input().split())
        nowPercent=int(Y*100/X)
        target=nowPercent+1
        #a번 더 이겼을때 퍼센트
        def percent(a):
            return int((Y+a)*100/(X+a))


        if nowPercent>=99:
            print(-1)
        else:
            left=0
            right=9999999999
            #처음으로 승률+1 이상이 나오는 부분을 찾아
            while(left<right):
                mid=(left+right)//2
                #print(left, right, mid)
                #print(percent(mid))
                if target<=percent(mid):
                    right=mid
                else:
                    left=mid+1
            print(right)
    except:
        break