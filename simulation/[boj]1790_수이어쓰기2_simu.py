def main():
    N,K=map(int,input().split())
    size=len(str(N))

    # 최대숫자구하기
    maxIndx=0
    maxNum="0"
    nowSize=0
    isPossible=False
    for digit in range(1,size):
        #print(digit)
        maxIndx+=9*(10**(digit-1))*digit
        maxNum+="9"
        nowSize+=1
        #print(maxNum,maxIndx,nowSize)
        if K<maxIndx:
            maxIndx-=9*(10**(digit-1))*digit
            maxNum=maxNum[:digit]
            isPossible=True
            break

    maxNum = int(maxNum)
    #마지막 자리수에있나?
    if not isPossible:
        lastMax=maxIndx+(N-maxNum)*size
        #print(lastMax)
        if lastMax<K:
            print(-1)
            return
        nowSize+=1
    #print("맥스넘버는", maxNum, "인덱스", maxIndx,"길이",nowSize)

    nowNum=maxNum+((K-maxIndx)//nowSize)
    if (K-maxIndx)%nowSize==0:
        print(str(nowNum)[-1])
    else:
        print(str(nowNum+1)[(K-maxIndx)%nowSize-1])

main()