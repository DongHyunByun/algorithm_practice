import sys
s,N,K,R1,R2,C1,C2=map(int,input().split())
#시간 0이면 그냥끝
if s==0:
    print("0")
    sys.exit()

#ans에 넣을때는 행은 -R1, 열은 -C1 꼭해줘라
ans=[["0" for j in range(C2-C1+1)] for i in range(R2-R1+1)]

for i in range(R1,R2+1):
    for j in range(C1,C2+1):
        for time in range(1,s+1):
            #홀수이면
            if N%2==1:
                if ((N**time)//2)-((N**(time-1))*K)//2 <= (i%(N**time)) <= ((N**time)//2)+((N**(time-1))*K)//2 and ((N**time)//2)-((N**(time-1))*K)//2 <= (j%(N**time)) <=((N**time)//2)+((N**(time-1))*K)//2:
                    ans[i-R1][j-C1]="1"
            #짝수이면
            else:
                if ((N**time)//2)-((N**(time-1))*K)//2 <= (i%(N**time)) < ((N**time)//2)+((N**(time-1))*K)//2 and ((N**time)//2)-((N**(time-1))*K)//2 <= (j%(N**time)) <((N**time)//2)+((N**(time-1))*K)//2:
                    ans[i - R1][j - C1] = "1"
            #색칠되면 다음꺼
            if ans[i-R1][j-C1]=="1":
                break

for i in ans:
    print("".join(i))

