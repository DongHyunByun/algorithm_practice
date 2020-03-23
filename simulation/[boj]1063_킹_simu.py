king,rock,N=input().split()
king=[8-int(king[1]),ord(king[0])-65]
rock=[8-int(rock[1]),ord(rock[0])-65]
move={"R":[0,1],"RB":[1,1],"B":[1,0],"LB":[1,-1],"L":[0,-1],"LT":[-1,-1],"T":[-1,0],"RT":[-1,1]}

for i in range(int(N)):
    order=input()
    kR=king[0]
    kC=king[1]
    rR=rock[0]
    rC=rock[1]

    kR+=move[order][0]
    kC+=move[order][1]

    if 0<=kR<8 and 0<=kC<8:
        #돌이랑 겹칠때
        if [kR,kC]==[rR,rC]:
            rR+=move[order][0]
            rC+=move[order][1]
            # 둘다이동가능 하면 이동
            if 0<=rR<8 and 0<=rC<8:
                rock=[rR,rC]
                king=[kR,kC]
        else:
            king=[kR,kC]

    else:
        continue

print(chr(king[1]+65)+str(8-king[0]))
print(chr(rock[1]+65)+str(8-rock[0]))