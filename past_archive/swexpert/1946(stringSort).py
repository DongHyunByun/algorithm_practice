for t in range(int(input())):
    ori=""
    for i in range(int(input())):
        [Ci,Ki]=input().split()
        ori=ori+(Ci*int(Ki))
    print(f"#{t+1}")
    for i in range(0,len(ori),10):
        print(ori[i:i+10])