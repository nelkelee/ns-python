a = 4
b = 9

## 이렇게 작성하는 것보다
for i in range(2, min(a,b)+1):
    print("check", i)
    if a%i==0 and b%i==0:
        print("not prime number")
        break
else:
        print("prime number")

## 도우미 함수를 써서 작성하되 loop에 false는 쓰지말자
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

assert coprime(4,9)
assert not coprime(3, 6)
