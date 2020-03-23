A, B, C = map(int, input().split())

def power(a,b):
    #1이면 끝
    if b==1:
        return a%C
    #짝수이면 제곱
    if b%2==0:
        return power(a**2%C,b//2)
    #홀수이면 곱하고 제곱
    else:
        return (a*power(a**2%C,b//2))%C

def main():
    print(power(A,B)%C)

main()