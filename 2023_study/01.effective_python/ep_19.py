# 19 함수가 여러 값을 반환하는 경우 절대로 네 값 이상을 언패킹하지 말라.

def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


def get_stats2(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    if count % 2 == 0:
        lower = sorted(numbers)[count//2 - 1]
        upper = sorted(numbers)[count//2]
        median = (lower + upper) / 2
    else:
        median = sorted(numbers)[count//2]

    return minimum, maximum, count, average, median #실수 유발하니 4개 이상 쓰지 않도록


print(get_stats([10,20,30,40])) #튜플로 리턴
a, b = get_stats([10,20,30,40])
print(a,b) #각각 리턴

print(get_stats2([10,20,30,40,50]))


