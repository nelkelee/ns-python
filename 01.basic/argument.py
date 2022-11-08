# 파이썬 3.2 부터 도입된 argparse는 cli 프로그램에서 더욱 다양한 argument 옵션을 가질 수 있다.

import argparse

#다음 코드는 정수 목록을 받아 합계 또는 최댓값을 출력하는 파이썬 프로그램입니다:
def parser_example1():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

#정말 간단히 쓴다면 아래도 좋겠다.
def parser_example2():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--date')
    args = parser.parse_args()
    print(args.date) #텍스트형태
    print(vars(args)) #딕셔너리형태

if __name__ == "__main__":
    parser_example2()