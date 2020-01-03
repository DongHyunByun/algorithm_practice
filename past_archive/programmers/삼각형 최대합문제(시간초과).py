'''
위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
'''

#리스트 버전
def recursive(depth,maxL,sum,index,tri):
    if depth==len(tri)-1 :
        if sum>maxL[0]:
            maxL[0]=sum

    else:
        for i in range(2):
            recursive(depth+1,maxL,sum+tri[depth+1][index+i],index+i,tri)

def solution(triangle):
    ans=[-100]
    recursive(0,ans,triangle[0][0],0,triangle)
    return ans[0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

#None이 나온다 이유는??? : 마지막에 return되는 maxL[0]이 해당 변수를 불러들이는 recursive함수로 가는데 
#이 함수는 return되지 않았기 때문이다! 따라서 ans를 글로벌 변수로 생각하여 ans를 반환하도록한다
# 굳이 ans을 list로 쓰는 이유는 aliasing이 되기 때문. int변수를 쓰면 복사가 되므로 글로벌 변수역할을 할 수 없다.




