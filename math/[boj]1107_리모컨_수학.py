def main():
    N=input()
    M=int(input())
    size=len(N)
    N=int(N)
    # 고장있을때와 없을 때
    if not M==0:
        broken=set(input().split())
        '''
        possible=set([i for i in range(10)])
        possible-=broken
        '''
    else:
        print(min(size, abs(int(N) - 100)))
        return

    # 전부다 고장일때
    if M==10:
        print(abs(int(N) - 100))
        return

    # 그외
    ans=[]
    ans.append(abs(int(N)-100))
    upNum=N
    downNum=N
    for i in range(500000):
        # 내려가는거
        if downNum != -1:
            downNumPos = True
            for j in str(downNum):
                if j in broken:
                    downNumPos = False
                    break

            if downNumPos:
                ans.append(i + len(str(downNum)))
                break
            else:
                downNum -= 1
        #올라가는거
        upNumPos=True
        for j in str(upNum):
            if j in broken:
                upNumPos=False
                break
        if upNumPos:
            ans.append(i+len(str(upNum)))
            break
        else:
            upNum += 1

    print(min(ans))


main()