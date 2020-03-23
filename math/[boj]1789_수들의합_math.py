S=int(input())
for i in range(1,9876543210):
    num=(i*i+i)//2
    if S<num:
        print(i-1)
        break






